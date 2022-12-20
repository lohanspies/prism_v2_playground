import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerificationPolicyInput")


@attr.s(auto_attribs=True)
class VerificationPolicyInput:
    """
    Example:
        {'issuerDIDs': ['issuerDIDs', 'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes', 'credentialTypes'],
            'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc)}

    Attributes:
        name (str):
        id (Union[Unset, str]):
        attributes (Union[Unset, List[str]]):
        issuer_di_ds (Union[Unset, List[str]]):
        credential_types (Union[Unset, List[str]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    name: str
    id: Union[Unset, str] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    issuer_di_ds: Union[Unset, List[str]] = UNSET
    credential_types: Union[Unset, List[str]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        issuer_di_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.issuer_di_ds, Unset):
            issuer_di_ds = self.issuer_di_ds

        credential_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.credential_types, Unset):
            credential_types = self.credential_types

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if issuer_di_ds is not UNSET:
            field_dict["issuerDIDs"] = issuer_di_ds
        if credential_types is not UNSET:
            field_dict["credentialTypes"] = credential_types
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        issuer_di_ds = cast(List[str], d.pop("issuerDIDs", UNSET))

        credential_types = cast(List[str], d.pop("credentialTypes", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        verification_policy_input = cls(
            name=name,
            id=id,
            attributes=attributes,
            issuer_di_ds=issuer_di_ds,
            credential_types=credential_types,
            created_at=created_at,
            updated_at=updated_at,
        )

        verification_policy_input.additional_properties = d
        return verification_policy_input

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
