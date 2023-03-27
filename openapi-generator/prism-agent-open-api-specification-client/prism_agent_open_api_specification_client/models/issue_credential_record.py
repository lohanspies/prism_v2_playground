import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.issue_credential_record_all_of_protocol_state import IssueCredentialRecordAllOfProtocolState
from ..models.issue_credential_record_all_of_role import IssueCredentialRecordAllOfRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_credential_record_base_claims import IssueCredentialRecordBaseClaims


T = TypeVar("T", bound="IssueCredentialRecord")


@attr.s(auto_attribs=True)
class IssueCredentialRecord:
    """An issue credential record that stores the state of the protocol execution.

    Attributes:
        claims (IssueCredentialRecordBaseClaims): The claims that will be associated with the issued verifiable
            credential.
        record_id (str): The unique identifier of the issue credential record.
        created_at (datetime.datetime): The date and time when the issue credential record was created.
        role (IssueCredentialRecordAllOfRole): The role played by the Prism agent in the credential issuance flow.
        protocol_state (IssueCredentialRecordAllOfProtocolState): The current state of the issue credential protocol
            execution.
        schema_id (Union[Unset, str]): The unique identifier of the schema used for this credential offer.
        subject_id (Union[Unset, str]): The identifier (e.g DID) of the subject to which the verifiable credential will
            be issued. Example: did:prism:subjectofverifiablecredentials.
        validity_period (Union[Unset, float]): The validity period in seconds of the verifiable credential that will be
            issued. Example: 3600.
        automatic_issuance (Union[Unset, bool]): Specifies whether or not the credential should be automatically
            generated and issued when receiving the `CredentialRequest` from the holder.
            If set to `false`, a manual approval by the issuer via API call will be required for the VC to be issued.
             Default: True.
        updated_at (Union[Unset, datetime.datetime]): The date and time when the issue credential record was last
            updated.
        jwt_credential (Union[Unset, str]): The base64-encoded JWT verifiable credential that has been sent by the
            issuer.
        issuing_did (Union[Unset, str]): Issuer DID of the verifiable credential object. Example:
            did:prism:issuerofverifiablecredentials.
    """

    claims: "IssueCredentialRecordBaseClaims"
    record_id: str
    created_at: datetime.datetime
    role: IssueCredentialRecordAllOfRole
    protocol_state: IssueCredentialRecordAllOfProtocolState
    schema_id: Union[Unset, str] = UNSET
    subject_id: Union[Unset, str] = UNSET
    validity_period: Union[Unset, float] = UNSET
    automatic_issuance: Union[Unset, bool] = True
    updated_at: Union[Unset, datetime.datetime] = UNSET
    jwt_credential: Union[Unset, str] = UNSET
    issuing_did: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        claims = self.claims.to_dict()

        record_id = self.record_id
        created_at = self.created_at.isoformat()

        role = self.role.value

        protocol_state = self.protocol_state.value

        schema_id = self.schema_id
        subject_id = self.subject_id
        validity_period = self.validity_period
        automatic_issuance = self.automatic_issuance
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        jwt_credential = self.jwt_credential
        issuing_did = self.issuing_did

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "claims": claims,
                "recordId": record_id,
                "createdAt": created_at,
                "role": role,
                "protocolState": protocol_state,
            }
        )
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if validity_period is not UNSET:
            field_dict["validityPeriod"] = validity_period
        if automatic_issuance is not UNSET:
            field_dict["automaticIssuance"] = automatic_issuance
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if jwt_credential is not UNSET:
            field_dict["jwtCredential"] = jwt_credential
        if issuing_did is not UNSET:
            field_dict["issuingDID"] = issuing_did

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_credential_record_base_claims import IssueCredentialRecordBaseClaims

        d = src_dict.copy()
        claims = IssueCredentialRecordBaseClaims.from_dict(d.pop("claims"))

        record_id = d.pop("recordId")

        created_at = isoparse(d.pop("createdAt"))

        role = IssueCredentialRecordAllOfRole(d.pop("role"))

        protocol_state = IssueCredentialRecordAllOfProtocolState(d.pop("protocolState"))

        schema_id = d.pop("schemaId", UNSET)

        subject_id = d.pop("subjectId", UNSET)

        validity_period = d.pop("validityPeriod", UNSET)

        automatic_issuance = d.pop("automaticIssuance", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        jwt_credential = d.pop("jwtCredential", UNSET)

        issuing_did = d.pop("issuingDID", UNSET)

        issue_credential_record = cls(
            claims=claims,
            record_id=record_id,
            created_at=created_at,
            role=role,
            protocol_state=protocol_state,
            schema_id=schema_id,
            subject_id=subject_id,
            validity_period=validity_period,
            automatic_issuance=automatic_issuance,
            updated_at=updated_at,
            jwt_credential=jwt_credential,
            issuing_did=issuing_did,
        )

        issue_credential_record.additional_properties = d
        return issue_credential_record

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
