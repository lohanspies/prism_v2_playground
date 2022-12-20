import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.issue_credential_record_all_of_protocol_state import IssueCredentialRecordAllOfProtocolState
from ..models.issue_credential_record_all_of_publication_state import IssueCredentialRecordAllOfPublicationState
from ..models.issue_credential_record_all_of_role import IssueCredentialRecordAllOfRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_issue_credential_record_request_claims import CreateIssueCredentialRecordRequestClaims


T = TypeVar("T", bound="IssueCredentialRecord")


@attr.s(auto_attribs=True)
class IssueCredentialRecord:
    """An issue credential record to store the state of the protocol execution

    Attributes:
        subject_id (str): Subject DID of the verifiable credentials object Example:
            did:prism:subjectofverifiablecredentials.
        claims (CreateIssueCredentialRecordRequestClaims): Claims that will be associated with given verifiable
            credentials
        record_id (str):
        created_at (datetime.datetime):
        role (IssueCredentialRecordAllOfRole):
        protocol_state (IssueCredentialRecordAllOfProtocolState):
        schema_id (Union[Unset, str]): Identifier of the VC Schema associated with this object
        validity_period (Union[Unset, float]): The validity period in seconds of the verifiable credential Example:
            3600.
        automatic_issuance (Union[Unset, bool]):  Default: True.
        await_confirmation (Union[Unset, bool]):  Default: True.
        updated_at (Union[Unset, datetime.datetime]):
        publication_state (Union[Unset, IssueCredentialRecordAllOfPublicationState]):
        jwt_credential (Union[Unset, str]):
    """

    subject_id: str
    claims: "CreateIssueCredentialRecordRequestClaims"
    record_id: str
    created_at: datetime.datetime
    role: IssueCredentialRecordAllOfRole
    protocol_state: IssueCredentialRecordAllOfProtocolState
    schema_id: Union[Unset, str] = UNSET
    validity_period: Union[Unset, float] = UNSET
    automatic_issuance: Union[Unset, bool] = True
    await_confirmation: Union[Unset, bool] = True
    updated_at: Union[Unset, datetime.datetime] = UNSET
    publication_state: Union[Unset, IssueCredentialRecordAllOfPublicationState] = UNSET
    jwt_credential: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_id = self.subject_id
        claims = self.claims.to_dict()

        record_id = self.record_id
        created_at = self.created_at.isoformat()

        role = self.role.value

        protocol_state = self.protocol_state.value

        schema_id = self.schema_id
        validity_period = self.validity_period
        automatic_issuance = self.automatic_issuance
        await_confirmation = self.await_confirmation
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        publication_state: Union[Unset, str] = UNSET
        if not isinstance(self.publication_state, Unset):
            publication_state = self.publication_state.value

        jwt_credential = self.jwt_credential

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subjectId": subject_id,
                "claims": claims,
                "recordId": record_id,
                "createdAt": created_at,
                "role": role,
                "protocolState": protocol_state,
            }
        )
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if validity_period is not UNSET:
            field_dict["validityPeriod"] = validity_period
        if automatic_issuance is not UNSET:
            field_dict["automaticIssuance"] = automatic_issuance
        if await_confirmation is not UNSET:
            field_dict["awaitConfirmation"] = await_confirmation
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if publication_state is not UNSET:
            field_dict["publicationState"] = publication_state
        if jwt_credential is not UNSET:
            field_dict["jwtCredential"] = jwt_credential

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_issue_credential_record_request_claims import CreateIssueCredentialRecordRequestClaims

        d = src_dict.copy()
        subject_id = d.pop("subjectId")

        claims = CreateIssueCredentialRecordRequestClaims.from_dict(d.pop("claims"))

        record_id = d.pop("recordId")

        created_at = isoparse(d.pop("createdAt"))

        role = IssueCredentialRecordAllOfRole(d.pop("role"))

        protocol_state = IssueCredentialRecordAllOfProtocolState(d.pop("protocolState"))

        schema_id = d.pop("schemaId", UNSET)

        validity_period = d.pop("validityPeriod", UNSET)

        automatic_issuance = d.pop("automaticIssuance", UNSET)

        await_confirmation = d.pop("awaitConfirmation", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _publication_state = d.pop("publicationState", UNSET)
        publication_state: Union[Unset, IssueCredentialRecordAllOfPublicationState]
        if isinstance(_publication_state, Unset):
            publication_state = UNSET
        else:
            publication_state = IssueCredentialRecordAllOfPublicationState(_publication_state)

        jwt_credential = d.pop("jwtCredential", UNSET)

        issue_credential_record = cls(
            subject_id=subject_id,
            claims=claims,
            record_id=record_id,
            created_at=created_at,
            role=role,
            protocol_state=protocol_state,
            schema_id=schema_id,
            validity_period=validity_period,
            automatic_issuance=automatic_issuance,
            await_confirmation=await_confirmation,
            updated_at=updated_at,
            publication_state=publication_state,
            jwt_credential=jwt_credential,
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
