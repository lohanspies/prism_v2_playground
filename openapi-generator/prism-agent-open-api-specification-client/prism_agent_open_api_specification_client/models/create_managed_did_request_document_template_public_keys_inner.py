from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.create_managed_did_request_document_template_public_keys_inner_purpose import (
    CreateManagedDidRequestDocumentTemplatePublicKeysInnerPurpose,
)

T = TypeVar("T", bound="CreateManagedDidRequestDocumentTemplatePublicKeysInner")


@attr.s(auto_attribs=True)
class CreateManagedDidRequestDocumentTemplatePublicKeysInner:
    """
    Example:
        {'purpose': 'authentication', 'id': 'key1'}

    Attributes:
        id (str): Identifier of a verification material in the DID Document Example: key1.
        purpose (CreateManagedDidRequestDocumentTemplatePublicKeysInnerPurpose):  Example: authentication.
    """

    id: str
    purpose: CreateManagedDidRequestDocumentTemplatePublicKeysInnerPurpose
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        purpose = self.purpose.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "purpose": purpose,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        purpose = CreateManagedDidRequestDocumentTemplatePublicKeysInnerPurpose(d.pop("purpose"))

        create_managed_did_request_document_template_public_keys_inner = cls(
            id=id,
            purpose=purpose,
        )

        create_managed_did_request_document_template_public_keys_inner.additional_properties = d
        return create_managed_did_request_document_template_public_keys_inner

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
