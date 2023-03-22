from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.service_type import ServiceType

T = TypeVar("T", bound="Service")


@attr.s(auto_attribs=True)
class Service:
    """A service expressed in the DID document.
    https://www.w3.org/TR/did-core/#services

        Example:
            {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type':
                'LinkedDomains'}

        Attributes:
            id (str):  Example: service-1.
            type (ServiceType): Service type.
                Can contain multiple possible values as described in the [Create DID operation](https://github.com/input-output-
                hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#create-did) under the construction section.

                *Known issue: This is currently misaligned with Prism DID method. This will be fixed in the future version of
                Prism Agent*
                 Example: LinkedDomains.
            service_endpoint (List[str]): Application service endpoints.
                Can contain multiple possible values as described in the [Create DID operation](https://github.com/input-output-
                hk/prism-did-method-spec/blob/main/w3c-spec/PRISM-method.md#create-did) under the construction section.

                *Known issue: This is currently misaligned with Prism DID method. This will be fixed in the future version of
                Prism Agent*
    """

    id: str
    type: ServiceType
    service_endpoint: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        service_endpoint = self.service_endpoint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "serviceEndpoint": service_endpoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = ServiceType(d.pop("type"))

        service_endpoint = cast(List[str], d.pop("serviceEndpoint"))

        service = cls(
            id=id,
            type=type,
            service_endpoint=service_endpoint,
        )

        service.additional_properties = d
        return service

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
