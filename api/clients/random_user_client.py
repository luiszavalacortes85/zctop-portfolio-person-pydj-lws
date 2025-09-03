import requests
from django.conf import settings
from .user_provider_strategy import UserProviderStrategy


class RandomUserClient(UserProviderStrategy):
    def get_user(self, nat="us"):
        r = requests.get(settings.RANDOMUSER_URL, params={"nat": nat}, timeout=5)
        r.raise_for_status()
        data = r.json()["results"][0]
        return {
            "first_name": data["name"]["first"],
            "last_name": data["name"]["last"],
            "country": data["location"]["country"],
            "nat": data["nat"],
        }