from enum import Enum


class ManagedDIDKeyTemplatePurpose(str, Enum):
    AUTHENTICATION = "authentication"
    ASSERTIONMETHOD = "assertionMethod"
    KEYAGREEMENT = "keyAgreement"
    CAPABILITYINVOCATION = "capabilityInvocation"
    CAPABILITYDELEGATION = "capabilityDelegation"

    def __str__(self) -> str:
        return str(self.value)
