from abc import ABC, abstractmethod


class UserProviderStrategy(ABC):
    """Interfaz Strategy para obtener usuarios"""

    @abstractmethod
    def get_user(self, nat="us"):
        pass