import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.issue_credential_record_all_of_protocol_state import IssueCredentialRecordAllOfProtocolState
from ..models.issue_credential_record_all_of_role import IssueCredentialRecordAllOfRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueCredentialRecordAllOf")


@attr.s(auto_attribs=True)
class IssueCredentialRecordAllOf:
    """
    Attributes:
        record_id (str): The unique identifier of the issue credential record.
        created_at (datetime.datetime): The date and time when the issue credential record was created.
        role (IssueCredentialRecordAllOfRole): The role played by the Prism agent in the credential issuance flow.
        protocol_state (IssueCredentialRecordAllOfProtocolState): The current state of the issue credential protocol
            execution.
        updated_at (Union[Unset, datetime.datetime]): The date and time when the issue credential record was last
            updated.
        jwt_credential (Union[Unset, str]): The base64-encoded JWT verifiable credential that has been sent by the
            issuer.
        issuing_did (Union[Unset, str]): Issuer DID of the verifiable credential object. Example:
            did:prism:issuerofverifiablecredentials.
    """

    record_id: str
    created_at: datetime.datetime
    role: IssueCredentialRecordAllOfRole
    protocol_state: IssueCredentialRecordAllOfProtocolState
    updated_at: Union[Unset, datetime.datetime] = UNSET
    jwt_credential: Union[Unset, str] = UNSET
    issuing_did: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        record_id = self.record_id
        created_at = self.created_at.isoformat()

        role = self.role.value

        protocol_state = self.protocol_state.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        jwt_credential = self.jwt_credential
        issuing_did = self.issuing_did

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recordId": record_id,
                "createdAt": created_at,
                "role": role,
                "protocolState": protocol_state,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if jwt_credential is not UNSET:
            field_dict["jwtCredential"] = jwt_credential
        if issuing_did is not UNSET:
            field_dict["issuingDID"] = issuing_did

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        record_id = d.pop("recordId")

        created_at = isoparse(d.pop("createdAt"))

        role = IssueCredentialRecordAllOfRole(d.pop("role"))

        protocol_state = IssueCredentialRecordAllOfProtocolState(d.pop("protocolState"))

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        jwt_credential = d.pop("jwtCredential", UNSET)

        issuing_did = d.pop("issuingDID", UNSET)

        issue_credential_record_all_of = cls(
            record_id=record_id,
            created_at=created_at,
            role=role,
            protocol_state=protocol_state,
            updated_at=updated_at,
            jwt_credential=jwt_credential,
            issuing_did=issuing_did,
        )

        issue_credential_record_all_of.additional_properties = d
        return issue_credential_record_all_of

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
