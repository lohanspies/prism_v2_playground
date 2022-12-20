from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.w3c_credential_status_status import W3CCredentialStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="W3CCredentialStatus")


@attr.s(auto_attribs=True)
class W3CCredentialStatus:
    """Verifiable Credential revocation status

    Example:
        {'description': 'Issued by did:prism:issuer12354 on 2022-02-01', 'status': 'issued'}

    Attributes:
        status (W3CCredentialStatusStatus): Status name Example: issued.
        description (Union[Unset, str]): Description about the status Example: Issued by did:prism:issuer12354 on
            2022-02-01.
    """

    status: W3CCredentialStatusStatus
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = W3CCredentialStatusStatus(d.pop("status"))

        description = d.pop("description", UNSET)

        w3c_credential_status = cls(
            status=status,
            description=description,
        )

        w3c_credential_status.additional_properties = d
        return w3c_credential_status

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
