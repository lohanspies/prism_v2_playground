import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerificationPolicy")


@attr.s(auto_attribs=True)
class VerificationPolicy:
    """
    Example:
        {'issuerDIDs': ['issuerDIDs', 'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'kind': 'kind', 'name': 'name', 'self': 'self', 'credentialTypes':
            ['credentialTypes', 'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}

    Attributes:
        self_ (str):
        kind (str):
        id (str):
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        attributes (Union[Unset, List[str]]):
        issuer_di_ds (Union[Unset, List[str]]):
        credential_types (Union[Unset, List[str]]):
    """

    self_: str
    kind: str
    id: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    attributes: Union[Unset, List[str]] = UNSET
    issuer_di_ds: Union[Unset, List[str]] = UNSET
    credential_types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_
        kind = self.kind
        id = self.id
        name = self.name
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        issuer_di_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.issuer_di_ds, Unset):
            issuer_di_ds = self.issuer_di_ds

        credential_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.credential_types, Unset):
            credential_types = self.credential_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "kind": kind,
                "id": id,
                "name": name,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if issuer_di_ds is not UNSET:
            field_dict["issuerDIDs"] = issuer_di_ds
        if credential_types is not UNSET:
            field_dict["credentialTypes"] = credential_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self")

        kind = d.pop("kind")

        id = d.pop("id")

        name = d.pop("name")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        attributes = cast(List[str], d.pop("attributes", UNSET))

        issuer_di_ds = cast(List[str], d.pop("issuerDIDs", UNSET))

        credential_types = cast(List[str], d.pop("credentialTypes", UNSET))

        verification_policy = cls(
            self_=self_,
            kind=kind,
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            attributes=attributes,
            issuer_di_ds=issuer_di_ds,
            credential_types=credential_types,
        )

        verification_policy.additional_properties = d
        return verification_policy

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
