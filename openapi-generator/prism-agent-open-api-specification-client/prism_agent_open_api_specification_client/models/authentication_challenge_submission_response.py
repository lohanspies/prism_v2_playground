from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationChallengeSubmissionResponse")


@attr.s(auto_attribs=True)
class AuthenticationChallengeSubmissionResponse:
    """
    Example:
        {'success': True, 'state': 'qrcode#123'}

    Attributes:
        success (bool):  Example: True.
        state (Union[Unset, str]): An opaque string provided by a relying-party indicating the purpose of
            this challenge in order to avoid repurposing the challenge submission.
             Example: qrcode#123.
    """

    success: bool
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        success = d.pop("success")

        state = d.pop("state", UNSET)

        authentication_challenge_submission_response = cls(
            success=success,
            state=state,
        )

        authentication_challenge_submission_response.additional_properties = d
        return authentication_challenge_submission_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
