from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.issue_credential_record import IssueCredentialRecord


T = TypeVar("T", bound="IssueCredentialRecordPageAllOf")


@attr.s(auto_attribs=True)
class IssueCredentialRecordPageAllOf:
    """
    Attributes:
        contents (List['IssueCredentialRecord']):
    """

    contents: List["IssueCredentialRecord"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contents = []
        for contents_item_data in self.contents:
            contents_item = contents_item_data.to_dict()

            contents.append(contents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contents": contents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_credential_record import IssueCredentialRecord

        d = src_dict.copy()
        contents = []
        _contents = d.pop("contents")
        for contents_item_data in _contents:
            contents_item = IssueCredentialRecord.from_dict(contents_item_data)

            contents.append(contents_item)

        issue_credential_record_page_all_of = cls(
            contents=contents,
        )

        issue_credential_record_page_all_of.additional_properties = d
        return issue_credential_record_page_all_of

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
