from enum import Enum


class ConnectionAllOfState(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

    INVITATIONGENERATED = 'InvitationGenerated'
    CONNECTIONRESPONSEPENDING = 'ConnectionResponsePending'
    CONNECTIONRESPONSESENT = 'ConnectionResponseSent'
    CONNECTIONREQUESTSENT = 'ConnectionRequestSent'
    CONNECTIONREQUESTPENDING = 'ConnectionRequestPending'
    CONNECTIONRESPONSERECEIVED = 'ConnectionResponseReceived'
    CONNECTIONREQUESTRECEIVED = 'ConnectionRequestReceived'
    def __str__(self) -> str:
        return str(self.value)
