from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.managed_did_key_template import ManagedDIDKeyTemplate
    from ..models.service import Service


T = TypeVar("T", bound="CreateManagedDidRequestDocumentTemplate")


@attr.s(auto_attribs=True)
class CreateManagedDidRequestDocumentTemplate:
    """
    Example:
        {'publicKeys': [{'purpose': 'authentication', 'id': 'key-1'}, {'purpose': 'authentication', 'id': 'key-1'}],
            'services': [{'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'],
            'type': 'LinkedDomains'}, {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/',
            'https://bar.example.com/'], 'type': 'LinkedDomains'}]}

    Attributes:
        public_keys (List['ManagedDIDKeyTemplate']):
        services (List['Service']):
    """

    public_keys: List["ManagedDIDKeyTemplate"]
    services: List["Service"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        public_keys = []
        for public_keys_item_data in self.public_keys:
            public_keys_item = public_keys_item_data.to_dict()

            public_keys.append(public_keys_item)

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()

            services.append(services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicKeys": public_keys,
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_did_key_template import ManagedDIDKeyTemplate
        from ..models.service import Service

        d = src_dict.copy()
        public_keys = []
        _public_keys = d.pop("publicKeys")
        for public_keys_item_data in _public_keys:
            public_keys_item = ManagedDIDKeyTemplate.from_dict(public_keys_item_data)

            public_keys.append(public_keys_item)

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = Service.from_dict(services_item_data)

            services.append(services_item)

        create_managed_did_request_document_template = cls(
            public_keys=public_keys,
            services=services,
        )

        create_managed_did_request_document_template.additional_properties = d
        return create_managed_did_request_document_template

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
