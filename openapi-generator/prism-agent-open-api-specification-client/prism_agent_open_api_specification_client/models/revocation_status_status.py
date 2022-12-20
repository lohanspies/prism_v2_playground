from enum import Enum


class RevocationStatusStatus(str, Enum):
    SCHEDULED = "scheduled"
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
