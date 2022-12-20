import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proof import Proof


T = TypeVar("T", bound="VerifiableCredentialSchema")


@attr.s(auto_attribs=True)
class VerifiableCredentialSchema:
    """
    Example:
        {'authored': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'author': 'author', 'name':
            'name', 'description': 'description', 'attributes': ['attributes', 'attributes'], 'id':
            '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'proof': {'proofValue': 'proofValue', 'created': datetime.datetime(2000,
            1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'domain': 'domain', 'proofPurpose': 'proofPurpose', 'type':
            'type', 'verificationMethod': 'verificationMethod'}, 'version': 'version', 'tags': ['tags', 'tags']}

    Attributes:
        id (str):
        name (str):
        version (str):
        author (str):
        authored (datetime.datetime):
        tags (Union[Unset, List[str]]):
        description (Union[Unset, str]):
        attributes (Union[Unset, List[str]]):
        proof (Union[Unset, Proof]):  Example: {'proofValue': 'proofValue', 'created': datetime.datetime(2000, 1, 23, 4,
            56, 7, tzinfo=datetime.timezone.utc), 'domain': 'domain', 'proofPurpose': 'proofPurpose', 'type': 'type',
            'verificationMethod': 'verificationMethod'}.
    """

    id: str
    name: str
    version: str
    author: str
    authored: datetime.datetime
    tags: Union[Unset, List[str]] = UNSET
    description: Union[Unset, str] = UNSET
    attributes: Union[Unset, List[str]] = UNSET
    proof: Union[Unset, "Proof"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        version = self.version
        author = self.author
        authored = self.authored.isoformat()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        description = self.description
        attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proof, Unset):
            proof = self.proof.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "version": version,
                "author": author,
                "authored": authored,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if description is not UNSET:
            field_dict["description"] = description
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if proof is not UNSET:
            field_dict["proof"] = proof

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proof import Proof

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        version = d.pop("version")

        author = d.pop("author")

        authored = isoparse(d.pop("authored"))

        tags = cast(List[str], d.pop("tags", UNSET))

        description = d.pop("description", UNSET)

        attributes = cast(List[str], d.pop("attributes", UNSET))

        _proof = d.pop("proof", UNSET)
        proof: Union[Unset, Proof]
        if isinstance(_proof, Unset):
            proof = UNSET
        else:
            proof = Proof.from_dict(_proof)

        verifiable_credential_schema = cls(
            id=id,
            name=name,
            version=version,
            author=author,
            authored=authored,
            tags=tags,
            description=description,
            attributes=attributes,
            proof=proof,
        )

        verifiable_credential_schema.additional_properties = d
        return verifiable_credential_schema

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
