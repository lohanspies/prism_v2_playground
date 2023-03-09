from enum import Enum


class ConnectionAllOfRole(str, Enum):
    INVITER = "Inviter"
    INVITEE = "Invitee"

    def __str__(self) -> str:
        return str(self.value)
