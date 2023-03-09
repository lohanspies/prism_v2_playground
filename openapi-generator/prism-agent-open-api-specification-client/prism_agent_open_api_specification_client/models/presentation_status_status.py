from enum import Enum


class PresentationStatusStatus(str, Enum):
    REQUESTPENDING = "RequestPending"
    REQUESTSENT = "RequestSent"
    REQUESTRECEIVED = "RequestReceived"
    REQUESTREJECTED = "RequestRejected"
    PRESENTATIONPENDING = "PresentationPending"
    PRESENTATIONGENERATED = "PresentationGenerated"
    PRESENTATIONSENT = "PresentationSent"
    PRESENTATIONRECEIVED = "PresentationReceived"
    PRESENTATIONVERIFIED = "PresentationVerified"
    PRESENTATIONACCEPTED = "PresentationAccepted"
    PRESENTATIONREJECTED = "PresentationRejected"
    PROBLEMREPORTPENDING = "ProblemReportPending"
    PROBLEMREPORTSENT = "ProblemReportSent"
    PROBLEMREPORTRECEIVED = "ProblemReportReceived"

    def __str__(self) -> str:
        return str(self.value)
