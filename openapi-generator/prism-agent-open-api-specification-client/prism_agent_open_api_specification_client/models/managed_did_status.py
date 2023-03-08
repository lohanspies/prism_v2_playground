from enum import Enum


class ManagedDIDStatus(str, Enum):
    CREATED = "CREATED"
    PUBLICATION_PENDING = "PUBLICATION_PENDING"
    PUBLISHED = "PUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
