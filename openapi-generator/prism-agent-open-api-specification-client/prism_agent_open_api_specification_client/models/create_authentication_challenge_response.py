from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAuthenticationChallengeResponse")


@attr.s(auto_attribs=True)
class CreateAuthenticationChallengeResponse:
    """
    Example:
        {'subject': 'did:example:123456789abcdefghi', 'challenge':
            'eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU'}

    Attributes:
        challenge (str): A JWT challenge that a user must provide to Castor SDK to create a ChallengeSubmission.
            JWT payload contains nonce, state, expiration, issuer
             Example: eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU.
        subject (Union[Unset, str]): A challenged subject that must complete the challenge.
            May refer to DID or VerificationMethod inside a DID. If VerificationMethod
            is used, it must be inside the authentication verification relationship.
             Example: did:example:123456789abcdefghi.
    """

    challenge: str
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge = self.challenge
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge": challenge,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        challenge = d.pop("challenge")

        subject = d.pop("subject", UNSET)

        create_authentication_challenge_response = cls(
            challenge=challenge,
            subject=subject,
        )

        create_authentication_challenge_response.additional_properties = d
        return create_authentication_challenge_response

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
