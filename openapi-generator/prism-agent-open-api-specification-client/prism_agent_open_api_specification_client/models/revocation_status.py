from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.revocation_status_status import RevocationStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RevocationStatus")


@attr.s(auto_attribs=True)
class RevocationStatus:
    """Revocation status record

    Example:
        {'id': 'operation1235', 'status': 'scheduled'}

    Attributes:
        id (Union[Unset, str]): Operation id Example: operation1235.
        status (Union[Unset, RevocationStatusStatus]): Operation status
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, RevocationStatusStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RevocationStatusStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RevocationStatusStatus(_status)

        revocation_status = cls(
            id=id,
            status=status,
        )

        revocation_status.additional_properties = d
        return revocation_status

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
