from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CreateIssueCredentialRecordRequestAllOf")


@attr.s(auto_attribs=True)
class CreateIssueCredentialRecordRequestAllOf:
    """
    Attributes:
        issuing_did (str): The issuer DID of the verifiable credential object. Example:
            did:prism:issuerofverifiablecredentials.
        connection_id (str): The unique identifier of a DIDComm connection that already exists between the issuer and
            the holder, and that will be used to execute the issue credential protocol.
    """

    issuing_did: str
    connection_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuing_did = self.issuing_did
        connection_id = self.connection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuingDID": issuing_did,
                "connectionId": connection_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issuing_did = d.pop("issuingDID")

        connection_id = d.pop("connectionId")

        create_issue_credential_record_request_all_of = cls(
            issuing_did=issuing_did,
            connection_id=connection_id,
        )

        create_issue_credential_record_request_all_of.additional_properties = d
        return create_issue_credential_record_request_all_of

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
