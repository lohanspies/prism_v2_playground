from enum import Enum


class ServiceType(str, Enum):
    MEDIATORSERVICE = "MediatorService"

    def __str__(self) -> str:
        return str(self.value)
