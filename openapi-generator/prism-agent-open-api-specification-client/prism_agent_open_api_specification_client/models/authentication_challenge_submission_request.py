from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AuthenticationChallengeSubmissionRequest")


@attr.s(auto_attribs=True)
class AuthenticationChallengeSubmissionRequest:
    """
    Example:
        {'signature': '243b9ed6561ab3...5d497f609b8cd04', 'subject': 'did:example:123456789abcdefghi', 'challenge':
            'eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU'}

    Attributes:
        challenge (str): A JWT challenge that a user must provide to Castor SDK to create a ChallengeSubmission.
            JWT payload contains nonce, state, expiration, issuer
             Example: eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU.
        subject (str): A challenged subject that must complete the challenge.
            May refer to DID or VerificationMethod inside a DID. If VerificationMethod
            is used, it must be inside the authentication verification relationship.
             Example: did:example:123456789abcdefghi.
        signature (str):  Example: 243b9ed6561ab3...5d497f609b8cd04.
    """

    challenge: str
    subject: str
    signature: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge = self.challenge
        subject = self.subject
        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge": challenge,
                "subject": subject,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        challenge = d.pop("challenge")

        subject = d.pop("subject")

        signature = d.pop("signature")

        authentication_challenge_submission_request = cls(
            challenge=challenge,
            subject=subject,
            signature=signature,
        )

        authentication_challenge_submission_request.additional_properties = d
        return authentication_challenge_submission_request

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
