# zctop-portfolio-person-pydj-lws
Portfolio de Persona un Lightweight Webservice en Python y DJango 

 source /home/${USER_NAME}/venv/bin/activate
 # 2. Instalar Django, DRF y requests
pip install django djangorestframework requests

# Crear proyecto (carpeta apiproxy)
django-admin startproject apiproxy .

# Crear app (la llamaremos api)
python manage.py startapp api

# Leer el archivo properties
pip install python-decouple

# OpenAPI Swagger
pip install drf-spectacular

python manage.py runserver

http://127.0.0.1:8000/api/random-name/
http://127.0.0.1:8000/api/random-name/?nat=es
http://127.0.0.1:8000/api/random-name/?nat=mx
http://127.0.0.1:8000/api/random-name/?provider=randomuser&nat=es
http://127.0.0.1:8000/api/random-name/?provider=faker&nat=es



