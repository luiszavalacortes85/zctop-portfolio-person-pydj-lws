import requests
from django.shortcuts import render
from rest_framework.decorators import api_view  # Para vistas basadas en función (FBV) en DRF
from rest_framework.response import Response      # Respuesta DRF con JSON por defecto
from rest_framework import status   # Códigos HTTP legibles
from .clients.random_user_client import RandomUserClient
from .clients.faker_user_client import FakerUserClient

@api_view(["GET"])  # <- Este endpoint solo acepta GET
def random_name(request):
    """
    Llama al API público https://randomuser.me/api/ y devuelve un nombre simplificado.
    Soporta un query param opcional ?nat= (nacionalidad) que randomuser entiende
    (ej: 'us', 'gb', 'es', 'fr', 'mx', etc).
    Ejemplos:
      /api/random-name/               -> usa 'us' por defecto
      /api/random-name/?nat=es        -> intenta español
      /api/random-name/?nat=mx        -> intenta México
    """
    # 1) Leer parámetro opcional 'nat' del query string; si no viene, usa 'us'
    nat = request.query_params.get("nat", "us")

    provider = request.query_params.get("provider", "randomuser")
    try:
        if provider == "faker":
            client = FakerUserClient()
        else:
            client = RandomUserClient()

        user = client.get_user(nat)
        return Response(user)

    except requests.exceptions.RequestException as e:
        # Cualquier problema de red/timeout/status no-2xx
        return Response(
            {
                "error": "No se pudo obtener datos del API externo",
                "details": str(e),  # Útil en desarrollo; en producción podrías omitirlo
            },
            status=status.HTTP_502_BAD_GATEWAY,
        )
    except (KeyError, ValueError, IndexError) as e:
        # Problemas al parsear la estructura del JSON
        return Response(
            {
                "error": "El API externo respondió en un formato inesperado",
                "details": str(e),
            },
            status=status.HTTP_502_BAD_GATEWAY,
        )