from enum import Enum


class VerificationMethodOrRefType(str, Enum):
    EMBEDDED = "EMBEDDED"
    REFERENCED = "REFERENCED"

    def __str__(self) -> str:
        return str(self.value)
