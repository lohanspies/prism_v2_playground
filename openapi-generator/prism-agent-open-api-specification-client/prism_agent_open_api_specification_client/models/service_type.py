from enum import Enum


class ServiceType(str, Enum):
    LINKEDDOMAINS = "LinkedDomains"

    def __str__(self) -> str:
        return str(self.value)
