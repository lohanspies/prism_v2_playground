from enum import Enum


class ConnectionAllOfState(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    INVITATION_GENERATED = 'InvitationGenerated'
    INVITATION_RECEIVED = 'InvitationReceived'
    CONNECTION_REQUEST_PENDING = 'ConnectionRequestPending'
    CONNECTION_REQUEST_SENT = 'ConnectionRequestSent'
    CONNECTION_REQUEST_RECEIVED = 'ConnectionRequestReceived'
    CONNECTION_RESPONSE_PENDING = 'ConnectionResponsePending'
    CONNECTION_RESPONSE_SENT = 'ConnectionResponseSent'
    CONNECTION_RESPONSE_RECEIVED = 'ConnectionResponseReceived'
    PROBLEM_REPORT_PENDING = 'ProblemReportPending'
    PROBLEM_REPORT_SENT = 'ProblemReportSent'

    def __str__(self) -> str:
        return str(self.value)
