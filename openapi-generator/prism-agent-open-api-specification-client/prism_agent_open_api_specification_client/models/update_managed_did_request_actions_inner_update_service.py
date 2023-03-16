from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.update_managed_did_request_actions_inner_update_service_type import (
    UpdateManagedDIDRequestActionsInnerUpdateServiceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateManagedDIDRequestActionsInnerUpdateService")


@attr.s(auto_attribs=True)
class UpdateManagedDIDRequestActionsInnerUpdateService:
    """A patch to existing Service. 'type' and 'serviceEndpoint' can't both be empty.

    Example:
        {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type':
            'LinkedDomains'}

    Attributes:
        id (str): ID of existing service to update in the DID document Example: service-1.
        type (Union[Unset, UpdateManagedDIDRequestActionsInnerUpdateServiceType]):  Example: LinkedDomains.
        service_endpoint (Union[Unset, List[str]]):
    """

    id: str
    type: Union[Unset, UpdateManagedDIDRequestActionsInnerUpdateServiceType] = UNSET
    service_endpoint: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        service_endpoint: Union[Unset, List[str]] = UNSET
        if not isinstance(self.service_endpoint, Unset):
            service_endpoint = self.service_endpoint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if service_endpoint is not UNSET:
            field_dict["serviceEndpoint"] = service_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        _type = d.pop("type", UNSET)
        type: Union[Unset, UpdateManagedDIDRequestActionsInnerUpdateServiceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = UpdateManagedDIDRequestActionsInnerUpdateServiceType(_type)

        service_endpoint = cast(List[str], d.pop("serviceEndpoint", UNSET))

        update_managed_did_request_actions_inner_update_service = cls(
            id=id,
            type=type,
            service_endpoint=service_endpoint,
        )

        update_managed_did_request_actions_inner_update_service.additional_properties = d
        return update_managed_did_request_actions_inner_update_service

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
