from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAuthenticationChallengeRequest")


@attr.s(auto_attribs=True)
class CreateAuthenticationChallengeRequest:
    """
    Example:
        {'subject': 'did:example:123456789abcdefghi', 'state': 'qrcode#123', 'ttl': 900}

    Attributes:
        ttl (float): A number of seconds that challenge will be considered valid. Example: 900.
        state (Union[Unset, str]): An opaque string provided by a relying-party indicating the purpose of
            this challenge in order to avoid repurposing the challenge submission.
             Example: qrcode#123.
        subject (Union[Unset, str]): A challenged subject that must complete the challenge.
            May refer to DID or VerificationMethod inside a DID. If VerificationMethod
            is used, it must be inside the authentication verification relationship.
             Example: did:example:123456789abcdefghi.
    """

    ttl: float
    state: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ttl = self.ttl
        state = self.state
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ttl": ttl,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ttl = d.pop("ttl")

        state = d.pop("state", UNSET)

        subject = d.pop("subject", UNSET)

        create_authentication_challenge_request = cls(
            ttl=ttl,
            state=state,
            subject=subject,
        )

        create_authentication_challenge_request.additional_properties = d
        return create_authentication_challenge_request

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
