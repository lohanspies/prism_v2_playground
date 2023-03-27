from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.update_managed_did_request_actions_inner_action_type import UpdateManagedDIDRequestActionsInnerActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_did_key_template import ManagedDIDKeyTemplate
    from ..models.service import Service
    from ..models.update_managed_did_request_actions_inner_remove_key import (
        UpdateManagedDIDRequestActionsInnerRemoveKey,
    )
    from ..models.update_managed_did_request_actions_inner_remove_service import (
        UpdateManagedDIDRequestActionsInnerRemoveService,
    )
    from ..models.update_managed_did_request_actions_inner_update_service import (
        UpdateManagedDIDRequestActionsInnerUpdateService,
    )


T = TypeVar("T", bound="UpdateManagedDIDRequestActionsInner")


@attr.s(auto_attribs=True)
class UpdateManagedDIDRequestActionsInner:
    """Detail of DID update action. Only property matching actionType can be present.

    Example:
        {'actionType': 'ADD_KEY', 'removeKey': {'id': 'key-1'}, 'removeService': {'id': 'service-1'}, 'addService':
            {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type':
            'LinkedDomains'}, 'updateService': {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/',
            'https://bar.example.com/'], 'type': 'LinkedDomains'}, 'addKey': {'purpose': 'authentication', 'id': 'key-1'}}

    Attributes:
        action_type (UpdateManagedDIDRequestActionsInnerActionType):  Example: ADD_KEY.
        add_key (Union[Unset, ManagedDIDKeyTemplate]): key-pair template to add to DID document. Example: {'purpose':
            'authentication', 'id': 'key-1'}.
        remove_key (Union[Unset, UpdateManagedDIDRequestActionsInnerRemoveKey]):  Example: {'id': 'key-1'}.
        add_service (Union[Unset, Service]): A service expressed in the DID document.
            https://www.w3.org/TR/did-core/#services
             Example: {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'],
            'type': 'LinkedDomains'}.
        remove_service (Union[Unset, UpdateManagedDIDRequestActionsInnerRemoveService]):  Example: {'id': 'service-1'}.
        update_service (Union[Unset, UpdateManagedDIDRequestActionsInnerUpdateService]): A patch to existing Service.
            'type' and 'serviceEndpoint' can't both be empty. Example: {'id': 'service-1', 'serviceEndpoint':
            ['https://bar.example.com/', 'https://bar.example.com/'], 'type': 'LinkedDomains'}.
    """

    action_type: UpdateManagedDIDRequestActionsInnerActionType
    add_key: Union[Unset, "ManagedDIDKeyTemplate"] = UNSET
    remove_key: Union[Unset, "UpdateManagedDIDRequestActionsInnerRemoveKey"] = UNSET
    add_service: Union[Unset, "Service"] = UNSET
    remove_service: Union[Unset, "UpdateManagedDIDRequestActionsInnerRemoveService"] = UNSET
    update_service: Union[Unset, "UpdateManagedDIDRequestActionsInnerUpdateService"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_type = self.action_type.value

        add_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_key, Unset):
            add_key = self.add_key.to_dict()

        remove_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remove_key, Unset):
            remove_key = self.remove_key.to_dict()

        add_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_service, Unset):
            add_service = self.add_service.to_dict()

        remove_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remove_service, Unset):
            remove_service = self.remove_service.to_dict()

        update_service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_service, Unset):
            update_service = self.update_service.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionType": action_type,
            }
        )
        if add_key is not UNSET:
            field_dict["addKey"] = add_key
        if remove_key is not UNSET:
            field_dict["removeKey"] = remove_key
        if add_service is not UNSET:
            field_dict["addService"] = add_service
        if remove_service is not UNSET:
            field_dict["removeService"] = remove_service
        if update_service is not UNSET:
            field_dict["updateService"] = update_service

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_did_key_template import ManagedDIDKeyTemplate
        from ..models.service import Service
        from ..models.update_managed_did_request_actions_inner_remove_key import (
            UpdateManagedDIDRequestActionsInnerRemoveKey,
        )
        from ..models.update_managed_did_request_actions_inner_remove_service import (
            UpdateManagedDIDRequestActionsInnerRemoveService,
        )
        from ..models.update_managed_did_request_actions_inner_update_service import (
            UpdateManagedDIDRequestActionsInnerUpdateService,
        )

        d = src_dict.copy()
        action_type = UpdateManagedDIDRequestActionsInnerActionType(d.pop("actionType"))

        _add_key = d.pop("addKey", UNSET)
        add_key: Union[Unset, ManagedDIDKeyTemplate]
        if isinstance(_add_key, Unset):
            add_key = UNSET
        else:
            add_key = ManagedDIDKeyTemplate.from_dict(_add_key)

        _remove_key = d.pop("removeKey", UNSET)
        remove_key: Union[Unset, UpdateManagedDIDRequestActionsInnerRemoveKey]
        if isinstance(_remove_key, Unset):
            remove_key = UNSET
        else:
            remove_key = UpdateManagedDIDRequestActionsInnerRemoveKey.from_dict(_remove_key)

        _add_service = d.pop("addService", UNSET)
        add_service: Union[Unset, Service]
        if isinstance(_add_service, Unset):
            add_service = UNSET
        else:
            add_service = Service.from_dict(_add_service)

        _remove_service = d.pop("removeService", UNSET)
        remove_service: Union[Unset, UpdateManagedDIDRequestActionsInnerRemoveService]
        if isinstance(_remove_service, Unset):
            remove_service = UNSET
        else:
            remove_service = UpdateManagedDIDRequestActionsInnerRemoveService.from_dict(_remove_service)

        _update_service = d.pop("updateService", UNSET)
        update_service: Union[Unset, UpdateManagedDIDRequestActionsInnerUpdateService]
        if isinstance(_update_service, Unset):
            update_service = UNSET
        else:
            update_service = UpdateManagedDIDRequestActionsInnerUpdateService.from_dict(_update_service)

        update_managed_did_request_actions_inner = cls(
            action_type=action_type,
            add_key=add_key,
            remove_key=remove_key,
            add_service=add_service,
            remove_service=remove_service,
            update_service=update_service,
        )

        update_managed_did_request_actions_inner.additional_properties = d
        return update_managed_did_request_actions_inner

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
