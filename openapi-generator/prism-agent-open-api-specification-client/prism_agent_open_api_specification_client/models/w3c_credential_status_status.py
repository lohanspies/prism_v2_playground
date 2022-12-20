from enum import Enum


class W3CCredentialStatusStatus(str, Enum):
    ISSUED = "issued"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
