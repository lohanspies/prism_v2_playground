from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_issue_credential_record_request_claims import CreateIssueCredentialRecordRequestClaims


T = TypeVar("T", bound="CreateIssueCredentialRecordRequest")


@attr.s(auto_attribs=True)
class CreateIssueCredentialRecordRequest:
    """A request to create a new "issue credential record"

    Example:
        {'validityPeriod': 3600, 'awaitConfirmation': True, 'schemaId': 'schemaId', 'claims': {'key': 'claims'},
            'automaticIssuance': True, 'subjectId': 'did:prism:subjectofverifiablecredentials'}

    Attributes:
        subject_id (str): Subject DID of the verifiable credentials object Example:
            did:prism:subjectofverifiablecredentials.
        claims (CreateIssueCredentialRecordRequestClaims): Claims that will be associated with given verifiable
            credentials
        schema_id (Union[Unset, str]): Identifier of the VC Schema associated with this object
        validity_period (Union[Unset, float]): The validity period in seconds of the verifiable credential Example:
            3600.
        automatic_issuance (Union[Unset, bool]):  Default: True.
        await_confirmation (Union[Unset, bool]):  Default: True.
    """

    subject_id: str
    claims: "CreateIssueCredentialRecordRequestClaims"
    schema_id: Union[Unset, str] = UNSET
    validity_period: Union[Unset, float] = UNSET
    automatic_issuance: Union[Unset, bool] = True
    await_confirmation: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject_id = self.subject_id
        claims = self.claims.to_dict()

        schema_id = self.schema_id
        validity_period = self.validity_period
        automatic_issuance = self.automatic_issuance
        await_confirmation = self.await_confirmation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subjectId": subject_id,
                "claims": claims,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_issue_credential_record_request_claims import CreateIssueCredentialRecordRequestClaims

        d = src_dict.copy()
        subject_id = d.pop("subjectId")

        claims = CreateIssueCredentialRecordRequestClaims.from_dict(d.pop("claims"))

        schema_id = d.pop("schemaId", UNSET)

        validity_period = d.pop("validityPeriod", UNSET)

        automatic_issuance = d.pop("automaticIssuance", UNSET)

        await_confirmation = d.pop("awaitConfirmation", UNSET)

        create_issue_credential_record_request = cls(
            subject_id=subject_id,
            claims=claims,
            schema_id=schema_id,
            validity_period=validity_period,
            automatic_issuance=automatic_issuance,
            await_confirmation=await_confirmation,
        )

        create_issue_credential_record_request.additional_properties = d
        return create_issue_credential_record_request

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
