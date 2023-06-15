from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateIssueCredentialRecordRequestClaims")


@attr.s(auto_attribs=True)
class CreateIssueCredentialRecordRequestClaims:
    """The claims that will be associated with the issued verifiable credential.

    Example:
        (firstname,Alice)

    """

    additional_properties: Dict[str, str] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        create_issue_credential_record_request_claims = cls()

        create_issue_credential_record_request_claims.additional_properties = d
        return create_issue_credential_record_request_claims

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties