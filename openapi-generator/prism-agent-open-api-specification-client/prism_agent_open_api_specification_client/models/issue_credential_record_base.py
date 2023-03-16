from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_credential_record_base_claims import IssueCredentialRecordBaseClaims


T = TypeVar("T", bound="IssueCredentialRecordBase")


@attr.s(auto_attribs=True)
class IssueCredentialRecordBase:
    """
    Attributes:
        claims (IssueCredentialRecordBaseClaims): The claims that will be associated with the issued verifiable
            credential.
        schema_id (Union[Unset, str]): The unique identifier of the schema used for this credential offer.
        subject_id (Union[Unset, str]): The identifier (e.g DID) of the subject to which the verifiable credential will
            be issued. Example: did:prism:subjectofverifiablecredentials.
        validity_period (Union[Unset, float]): The validity period in seconds of the verifiable credential that will be
            issued. Example: 3600.
        automatic_issuance (Union[Unset, bool]): Specifies whether or not the credential should be automatically
            generated and issued when receiving the `CredentialRequest` from the holder.
            If set to `false`, a manual approval by the issuer via API call will be required for the VC to be issued.
             Default: True.
    """

    claims: "IssueCredentialRecordBaseClaims"
    schema_id: Union[Unset, str] = UNSET
    subject_id: Union[Unset, str] = UNSET
    validity_period: Union[Unset, float] = UNSET
    automatic_issuance: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        claims = self.claims.to_dict()

        schema_id = self.schema_id
        subject_id = self.subject_id
        validity_period = self.validity_period
        automatic_issuance = self.automatic_issuance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "claims": claims,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.issue_credential_record_base_claims import IssueCredentialRecordBaseClaims

        d = src_dict.copy()
        claims = IssueCredentialRecordBaseClaims.from_dict(d.pop("claims"))

        schema_id = d.pop("schemaId", UNSET)

        subject_id = d.pop("subjectId", UNSET)

        validity_period = d.pop("validityPeriod", UNSET)

        automatic_issuance = d.pop("automaticIssuance", UNSET)

        issue_credential_record_base = cls(
            claims=claims,
            schema_id=schema_id,
            subject_id=subject_id,
            validity_period=validity_period,
            automatic_issuance=automatic_issuance,
        )

        issue_credential_record_base.additional_properties = d
        return issue_credential_record_base

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
