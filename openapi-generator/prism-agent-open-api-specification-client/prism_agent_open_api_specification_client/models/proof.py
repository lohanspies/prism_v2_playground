import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Proof")


@attr.s(auto_attribs=True)
class Proof:
    """
    Example:
        {'proofValue': 'proofValue', 'created': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc),
            'domain': 'domain', 'proofPurpose': 'proofPurpose', 'type': 'type', 'verificationMethod': 'verificationMethod'}

    Attributes:
        type (str):
        created (datetime.datetime):
        verification_method (str):
        proof_purpose (str):
        proof_value (str):
        domain (Union[Unset, str]):
    """

    type: str
    created: datetime.datetime
    verification_method: str
    proof_purpose: str
    proof_value: str
    domain: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        created = self.created.isoformat()

        verification_method = self.verification_method
        proof_purpose = self.proof_purpose
        proof_value = self.proof_value
        domain = self.domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "created": created,
                "verificationMethod": verification_method,
                "proofPurpose": proof_purpose,
                "proofValue": proof_value,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        created = isoparse(d.pop("created"))

        verification_method = d.pop("verificationMethod")

        proof_purpose = d.pop("proofPurpose")

        proof_value = d.pop("proofValue")

        domain = d.pop("domain", UNSET)

        proof = cls(
            type=type,
            created=created,
            verification_method=verification_method,
            proof_purpose=proof_purpose,
            proof_value=proof_value,
            domain=domain,
        )

        proof.additional_properties = d
        return proof

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
