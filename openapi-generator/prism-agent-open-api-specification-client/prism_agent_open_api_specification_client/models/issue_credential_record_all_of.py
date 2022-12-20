import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.issue_credential_record_all_of_protocol_state import IssueCredentialRecordAllOfProtocolState
from ..models.issue_credential_record_all_of_publication_state import IssueCredentialRecordAllOfPublicationState
from ..models.issue_credential_record_all_of_role import IssueCredentialRecordAllOfRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueCredentialRecordAllOf")


@attr.s(auto_attribs=True)
class IssueCredentialRecordAllOf:
    """
    Attributes:
        record_id (str):
        created_at (datetime.datetime):
        role (IssueCredentialRecordAllOfRole):
        protocol_state (IssueCredentialRecordAllOfProtocolState):
        updated_at (Union[Unset, datetime.datetime]):
        publication_state (Union[Unset, IssueCredentialRecordAllOfPublicationState]):
        jwt_credential (Union[Unset, str]):
    """

    record_id: str
    created_at: datetime.datetime
    role: IssueCredentialRecordAllOfRole
    protocol_state: IssueCredentialRecordAllOfProtocolState
    updated_at: Union[Unset, datetime.datetime] = UNSET
    publication_state: Union[Unset, IssueCredentialRecordAllOfPublicationState] = UNSET
    jwt_credential: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        record_id = self.record_id
        created_at = self.created_at.isoformat()

        role = self.role.value

        protocol_state = self.protocol_state.value

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
                "recordId": record_id,
                "createdAt": created_at,
                "role": role,
                "protocolState": protocol_state,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if publication_state is not UNSET:
            field_dict["publicationState"] = publication_state
        if jwt_credential is not UNSET:
            field_dict["jwtCredential"] = jwt_credential

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

        _publication_state = d.pop("publicationState", UNSET)
        publication_state: Union[Unset, IssueCredentialRecordAllOfPublicationState]
        if isinstance(_publication_state, Unset):
            publication_state = UNSET
        else:
            publication_state = IssueCredentialRecordAllOfPublicationState(_publication_state)

        jwt_credential = d.pop("jwtCredential", UNSET)

        issue_credential_record_all_of = cls(
            record_id=record_id,
            created_at=created_at,
            role=role,
            protocol_state=protocol_state,
            updated_at=updated_at,
            publication_state=publication_state,
            jwt_credential=jwt_credential,
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
