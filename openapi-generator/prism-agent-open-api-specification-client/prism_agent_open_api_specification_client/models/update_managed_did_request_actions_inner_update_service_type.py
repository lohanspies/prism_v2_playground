from enum import Enum


class UpdateManagedDIDRequestActionsInnerUpdateServiceType(str, Enum):
    LINKEDDOMAINS = "LinkedDomains"

    def __str__(self) -> str:
        return str(self.value)
