from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DidOperationSubmission")


@attr.s(auto_attribs=True)
class DidOperationSubmission:
    """
    Example:
        {'id': '123', 'didRef': 'did:prism:123'}

    Attributes:
        id (str):  Example: 123.
        did_ref (str):  Example: did:prism:123.
    """

    id: str
    did_ref: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        did_ref = self.did_ref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "didRef": did_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        did_ref = d.pop("didRef")

        did_operation_submission = cls(
            id=id,
            did_ref=did_ref,
        )

        did_operation_submission.additional_properties = d
        return did_operation_submission

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
