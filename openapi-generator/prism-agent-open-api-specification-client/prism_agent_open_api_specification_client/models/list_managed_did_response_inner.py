from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_managed_did_response_inner_status import ListManagedDIDResponseInnerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListManagedDIDResponseInner")


@attr.s(auto_attribs=True)
class ListManagedDIDResponseInner:
    """
    Example:
        {'longFormDid': 'did:prism:abc:123', 'did': 'did:prism:abc', 'status': 'CREATED'}

    Attributes:
        did (str):  Example: did:prism:abc.
        status (ListManagedDIDResponseInnerStatus): A status indicating whether this is already published from the
            wallet or not. Does not represent DID full lifecyle (e.g. deactivated, recovered, updated).
        long_form_did (Union[Unset, str]): A long-form DID. Mandatory when status is not PUBLISHED and optional when
            status is PUBLISHED Example: did:prism:abc:123.
    """

    did: str
    status: ListManagedDIDResponseInnerStatus
    long_form_did: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        did = self.did
        status = self.status.value

        long_form_did = self.long_form_did

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "did": did,
                "status": status,
            }
        )
        if long_form_did is not UNSET:
            field_dict["longFormDid"] = long_form_did

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        did = d.pop("did")

        status = ListManagedDIDResponseInnerStatus(d.pop("status"))

        long_form_did = d.pop("longFormDid", UNSET)

        list_managed_did_response_inner = cls(
            did=did,
            status=status,
            long_form_did=long_form_did,
        )

        list_managed_did_response_inner.additional_properties = d
        return list_managed_did_response_inner

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
