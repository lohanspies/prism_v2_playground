import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerificationCredentialSchemaInput")


@attr.s(auto_attribs=True)
class VerificationCredentialSchemaInput:
    """
    Example:
        {'authored': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'name': 'name',
            'description': 'description', 'attributes': ['attributes', 'attributes'], 'id':
            '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'version': 'version', 'tags': ['tags', 'tags']}

    Attributes:
        name (str):
        version (str):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        attributes (Union[Unset, List[str]]):
        authored (Union[Unset, datetime.datetime]):
        tags (Union[Unset, List[str]]):
    """

    name: str
    version: str
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    authored: Union[Unset, datetime.datetime] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        version = self.version
        id = self.id
        description = self.description
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        authored: Union[Unset, str] = UNSET
        if not isinstance(self.authored, Unset):
            authored = self.authored.isoformat()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if authored is not UNSET:
            field_dict["authored"] = authored
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        version = d.pop("version")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        _authored = d.pop("authored", UNSET)
        authored: Union[Unset, datetime.datetime]
        if isinstance(_authored, Unset):
            authored = UNSET
        else:
            authored = isoparse(_authored)

        tags = cast(List[str], d.pop("tags", UNSET))

        verification_credential_schema_input = cls(
            name=name,
            version=version,
            id=id,
            description=description,
            attributes=attributes,
            authored=authored,
            tags=tags,
        )

        verification_credential_schema_input.additional_properties = d
        return verification_credential_schema_input

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
