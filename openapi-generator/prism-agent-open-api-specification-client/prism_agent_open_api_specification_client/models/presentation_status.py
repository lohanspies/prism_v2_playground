from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proof_request_aux import ProofRequestAux


T = TypeVar("T", bound="PresentationStatus")


@attr.s(auto_attribs=True)
class PresentationStatus:
    """Presentation Status

    Example:
        {'presentationId': 'presentationId', 'proofs': [{'schemaId': 'https://schema.org/Person', 'trustIssuers':
            ['did:web:atalaprism.io/users/testUser', 'did.prism:123', 'did:prism:...']}, {'schemaId':
            'https://schema.org/Person', 'trustIssuers': ['did:web:atalaprism.io/users/testUser', 'did.prism:123',
            'did:prism:...']}], 'connectionId': 'connectionId', 'status': 'status'}

    Attributes:
        presentation_id (str):
        status (str):
        proofs (List['ProofRequestAux']):
        connection_id (Union[Unset, str]):
    """

    presentation_id: str
    status: str
    proofs: List["ProofRequestAux"]
    connection_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        presentation_id = self.presentation_id
        status = self.status
        proofs = []
        for proofs_item_data in self.proofs:
            proofs_item = proofs_item_data.to_dict()

            proofs.append(proofs_item)

        connection_id = self.connection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "presentationId": presentation_id,
                "status": status,
                "proofs": proofs,
            }
        )
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proof_request_aux import ProofRequestAux

        d = src_dict.copy()
        presentation_id = d.pop("presentationId")

        status = d.pop("status")

        proofs = []
        _proofs = d.pop("proofs")
        for proofs_item_data in _proofs:
            proofs_item = ProofRequestAux.from_dict(proofs_item_data)

            proofs.append(proofs_item)

        connection_id = d.pop("connectionId", UNSET)

        presentation_status = cls(
            presentation_id=presentation_id,
            status=status,
            proofs=proofs,
            connection_id=connection_id,
        )

        presentation_status.additional_properties = d
        return presentation_status

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
