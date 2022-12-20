from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revocation_status import RevocationStatus


T = TypeVar("T", bound="W3CCredentialRevocationResponse")


@attr.s(auto_attribs=True)
class W3CCredentialRevocationResponse:
    """Credential revocation response. Contain credential id and revocation operation for tracing the completion

    Example:
        {'credentialId': 'abcde-12345', 'operation': {'id': 'operation1235', 'status': 'scheduled'}}

    Attributes:
        credential_id (str): Credential identity Example: abcde-12345.
        operation (Union[Unset, RevocationStatus]): Revocation status record Example: {'id': 'operation1235', 'status':
            'scheduled'}.
    """

    credential_id: str
    operation: Union[Unset, "RevocationStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credential_id = self.credential_id
        operation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialId": credential_id,
            }
        )
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.revocation_status import RevocationStatus

        d = src_dict.copy()
        credential_id = d.pop("credentialId")

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, RevocationStatus]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = RevocationStatus.from_dict(_operation)

        w3c_credential_revocation_response = cls(
            credential_id=credential_id,
            operation=operation,
        )

        w3c_credential_revocation_response.additional_properties = d
        return w3c_credential_revocation_response

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
