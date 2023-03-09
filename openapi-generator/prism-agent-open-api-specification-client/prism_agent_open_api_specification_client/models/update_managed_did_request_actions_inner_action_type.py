from enum import Enum


class UpdateManagedDIDRequestActionsInnerActionType(str, Enum):
    ADD_KEY = "ADD_KEY"
    REMOVE_KEY = "REMOVE_KEY"
    ADD_SERVICE = "ADD_SERVICE"
    REMOVE_SERVICE = "REMOVE_SERVICE"
    UPDATE_SERVICE = "UPDATE_SERVICE"

    def __str__(self) -> str:
        return str(self.value)
