from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.issue_credential_record import IssueCredentialRecord


T = TypeVar("T", bound="IssueCredentialRecordCollection")


@attr.s(auto_attribs=True)
class IssueCredentialRecordCollection:
    """A collection of issue credential records

    Example:
        {'offset': 0, 'limit': 6, 'count': 1, 'items': [None, None]}

    Attributes:
        items (List['IssueCredentialRecord']):
        offset (int):
        limit (int):
        count (int):
    """

    items: List["IssueCredentialRecord"]
    offset: int
    limit: int
    count: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()

            items.append(items_item)

        offset = self.offset
        limit = self.limit
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "offset": offset,
                "limit": limit,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_credential_record import IssueCredentialRecord

        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = IssueCredentialRecord.from_dict(items_item_data)

            items.append(items_item)

        offset = d.pop("offset")

        limit = d.pop("limit")

        count = d.pop("count")

        issue_credential_record_collection = cls(
            items=items,
            offset=offset,
            limit=limit,
            count=count,
        )

        issue_credential_record_collection.additional_properties = d
        return issue_credential_record_collection

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
