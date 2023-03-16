from enum import Enum


class IssueCredentialRecordAllOfProtocolState(str, Enum):
    OFFERPENDING = "OfferPending"
    OFFERSENT = "OfferSent"
    OFFERRECEIVED = "OfferReceived"
    REQUESTPENDING = "RequestPending"
    REQUESTGENERATED = "RequestGenerated"
    REQUESTSENT = "RequestSent"
    REQUESTRECEIVED = "RequestReceived"
    PROBLEMREPORTPENDING = "ProblemReportPending"
    PROBLEMREPORTSENT = "ProblemReportSent"
    PROBLEMREPORTRECEIVED = "ProblemReportReceived"
    CREDENTIALPENDING = "CredentialPending"
    CREDENTIALSENT = "CredentialSent"
    CREDENTIALRECEIVED = "CredentialReceived"
    CREDENTIALGENERATED = "CredentialGenerated"

    def __str__(self) -> str:
        return str(self.value)
