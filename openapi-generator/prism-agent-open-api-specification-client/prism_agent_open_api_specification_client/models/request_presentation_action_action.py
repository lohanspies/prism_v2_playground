from enum import Enum


class RequestPresentationActionAction(str, Enum):
    REQUEST_ACCEPT = "request-accept"
    REQUEST_REJECT = "request-reject"
    PRESENTATION_ACCEPT = "presentation-accept"
    PRESENTATION_REJECT = "presentation-reject"

    def __str__(self) -> str:
        return str(self.value)
