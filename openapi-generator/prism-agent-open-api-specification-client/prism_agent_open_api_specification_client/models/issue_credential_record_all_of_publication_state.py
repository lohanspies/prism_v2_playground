from enum import Enum


class IssueCredentialRecordAllOfPublicationState(str, Enum):
    PUBLICATIONPENDING = "PublicationPending"
    PUBLICATIONQUEUED = "PublicationQueued"
    PUBLISHED = "Published"

    def __str__(self) -> str:
        return str(self.value)
