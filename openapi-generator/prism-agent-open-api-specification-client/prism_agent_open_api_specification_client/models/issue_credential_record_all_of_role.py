from enum import Enum


class IssueCredentialRecordAllOfRole(str, Enum):
    ISSUER = "Issuer"
    HOLDER = "Holder"

    def __str__(self) -> str:
        return str(self.value)
