from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="W3CCredentialRevocationRequest")


@attr.s(auto_attribs=True)
class W3CCredentialRevocationRequest:
    """Credential revocation request. Contain credential id and other information required for revocation

    Example:
        {'credentialId': 'abcde-12345'}

    Attributes:
        credential_id (str): Credential identity Example: abcde-12345.
    """

    credential_id: str

    def to_dict(self) -> Dict[str, Any]:
        credential_id = self.credential_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "credentialId": credential_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credential_id = d.pop("credentialId")

        w3c_credential_revocation_request = cls(
            credential_id=credential_id,
        )

        return w3c_credential_revocation_request
