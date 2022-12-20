from enum import Enum


class CreateManagedDidRequestDocumentTemplatePublicKeysInnerPurpose(str, Enum):
    AUTHENTICATION = "authentication"
    ASSERTIONMETHOD = "assertionMethod"
    KEYAGREEMENT = "keyAgreement"
    CAPABILITYINVOCATION = "capabilityInvocation"
    CAPABILITYDELEGATION = "capabilityDelegation"

    def __str__(self) -> str:
        return str(self.value)
