from enum import Enum


class ConnectionAllOfState(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    # TODO - make all values UPPERCASE in ENUM
    InvitationGenerated = 'InvitationGenerated'
    ConnectionResponsePending = 'ConnectionResponsePending'
    ConnectionResponseSent = 'ConnectionResponseSent'
    ConnectionRequestSent = 'ConnectionRequestSent'
    ConnectionRequestPending = 'ConnectionRequestPending'
    ConnectionResponseReceived = 'ConnectionResponseReceived'

    def __str__(self) -> str:
        return str(self.value)
