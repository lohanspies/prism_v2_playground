from enum import Enum


class ConnectionAllOfState(str, Enum):
    INVITATIONGENERATED = "InvitationGenerated"
    INVITATIONRECEIVED = "InvitationReceived"
    CONNECTIONREQUESTPENDING = "ConnectionRequestPending"
    CONNECTIONREQUESTSENT = "ConnectionRequestSent"
    CONNECTIONREQUESTRECEIVED = "ConnectionRequestReceived"
    CONNECTIONRESPONSEPENDING = "ConnectionResponsePending"
    CONNECTIONRESPONSESENT = "ConnectionResponseSent"
    CONNECTIONRESPONSERECEIVED = "ConnectionResponseReceived"
    PROBLEMREPORTPENDING = "ProblemReportPending"
    PROBLEMREPORTSENT = "ProblemReportSent"
    PROBLEMREPORTRECEIVED = "ProblemReportReceived"

    def __str__(self) -> str:
        return str(self.value)
