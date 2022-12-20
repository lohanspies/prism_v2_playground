from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.proof_request_aux import ProofRequestAux


T = TypeVar("T", bound="RequestPresentationInput")


@attr.s(auto_attribs=True)
class RequestPresentationInput:
    """Request Presentation Input

    Example:
        {'proofs': [{'schemaId': 'https://schema.org/Person', 'trustIssuers': ['did:web:atalaprism.io/users/testUser',
            'did.prism:123', 'did:prism:...']}, {'schemaId': 'https://schema.org/Person', 'trustIssuers':
            ['did:web:atalaprism.io/users/testUser', 'did.prism:123', 'did:prism:...']}], 'connectionId': 'connectionId'}

    Attributes:
        connection_id (str):
        proofs (List['ProofRequestAux']):
    """

    connection_id: str
    proofs: List["ProofRequestAux"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        proofs = []
        for proofs_item_data in self.proofs:
            proofs_item = proofs_item_data.to_dict()

            proofs.append(proofs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
                "proofs": proofs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.proof_request_aux import ProofRequestAux

        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        proofs = []
        _proofs = d.pop("proofs")
        for proofs_item_data in _proofs:
            proofs_item = ProofRequestAux.from_dict(proofs_item_data)

            proofs.append(proofs_item)

        request_presentation_input = cls(
            connection_id=connection_id,
            proofs=proofs,
        )

        request_presentation_input.additional_properties = d
        return request_presentation_input

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
