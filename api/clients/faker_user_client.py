import requests
from django.conf import settings
from .user_provider_strategy import UserProviderStrategy


class FakerUserClient(UserProviderStrategy):
    def get_user(self, nat="us"):
        r = requests.get(settings.FAKER_URL, params={"_locale": nat}, timeout=5)
        r.raise_for_status()
        data = r.json()["data"][0]
        return {
            "first_name": data["firstname"],
            "last_name": data["lastname"],
            "country": data.get("address", "Unknown"),
            "nat": nat.upper(),
        }