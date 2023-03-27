from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.update_managed_did_request_actions_inner import UpdateManagedDIDRequestActionsInner


T = TypeVar("T", bound="UpdateManagedDIDRequest")


@attr.s(auto_attribs=True)
class UpdateManagedDIDRequest:
    """
    Example:
        {'actions': [{'actionType': 'ADD_KEY', 'removeKey': {'id': 'key-1'}, 'removeService': {'id': 'service-1'},
            'addService': {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'],
            'type': 'LinkedDomains'}, 'updateService': {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/',
            'https://bar.example.com/'], 'type': 'LinkedDomains'}, 'addKey': {'purpose': 'authentication', 'id': 'key-1'}},
            {'actionType': 'ADD_KEY', 'removeKey': {'id': 'key-1'}, 'removeService': {'id': 'service-1'}, 'addService':
            {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type':
            'LinkedDomains'}, 'updateService': {'id': 'service-1', 'serviceEndpoint': ['https://bar.example.com/',
            'https://bar.example.com/'], 'type': 'LinkedDomains'}, 'addKey': {'purpose': 'authentication', 'id': 'key-1'}}]}

    Attributes:
        actions (List['UpdateManagedDIDRequestActionsInner']): A list of actions to perform on DID document.
            The field `addKey`, `removeKey`, `addService`, `removeService`, `updateService` must corresponds to
            the `actionType` specified. For example, `addKey` must be present when `actionType` is `ADD_KEY`.
    """

    actions: List["UpdateManagedDIDRequestActionsInner"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_managed_did_request_actions_inner import UpdateManagedDIDRequestActionsInner

        d = src_dict.copy()
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = UpdateManagedDIDRequestActionsInner.from_dict(actions_item_data)

            actions.append(actions_item)

        update_managed_did_request = cls(
            actions=actions,
        )

        update_managed_did_request.additional_properties = d
        return update_managed_did_request

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
