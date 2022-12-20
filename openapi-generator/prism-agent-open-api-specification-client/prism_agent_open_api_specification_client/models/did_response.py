from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.did import DID
    from ..models.did_document_metadata import DIDDocumentMetadata


T = TypeVar("T", bound="DIDResponse")


@attr.s(auto_attribs=True)
class DIDResponse:
    """
    Example:
        {'metadata': {'deactivated': True}, 'did': {'assertionMethod': [{'controller': 'did:prism:456', 'publicKeyJwk':
            {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456',
            'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'controller': 'did:prism:mainnet:456',
            'service': [{'id': 'service1', 'serviceEndpoint': ['https://bar.example.com', 'https://bar.example.com'],
            'type': 'MediatorService'}, {'id': 'service1', 'serviceEndpoint': ['https://bar.example.com',
            'https://bar.example.com'], 'type': 'MediatorService'}], 'keyAgreement': [{'controller': 'did:prism:456',
            'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456',
            'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'id': 'did:prism:mainnet:123',
            'verificationMethod': [{'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid':
            '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id': 'did:prism:123#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'capabilityInvocation': [{'controller':
            'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid':
            '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id': 'did:prism:123#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'authentication': [{'controller':
            'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid':
            '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id': 'did:prism:123#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}]}}

    Attributes:
        did (DID):  Example: {'assertionMethod': [{'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456',
            'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'controller': 'did:prism:mainnet:456',
            'service': [{'id': 'service1', 'serviceEndpoint': ['https://bar.example.com', 'https://bar.example.com'],
            'type': 'MediatorService'}, {'id': 'service1', 'serviceEndpoint': ['https://bar.example.com',
            'https://bar.example.com'], 'type': 'MediatorService'}], 'keyAgreement': [{'controller': 'did:prism:456',
            'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456',
            'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'id': 'did:prism:mainnet:123',
            'verificationMethod': [{'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid':
            '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id': 'did:prism:123#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'capabilityInvocation': [{'controller':
            'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid':
            '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id': 'did:prism:123#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}], 'authentication': [{'controller':
            'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid':
            '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id': 'did:prism:123#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}]}.
        metadata (DIDDocumentMetadata):  Example: {'deactivated': True}.
    """

    did: "DID"
    metadata: "DIDDocumentMetadata"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        did = self.did.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "did": did,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.did import DID
        from ..models.did_document_metadata import DIDDocumentMetadata

        d = src_dict.copy()
        did = DID.from_dict(d.pop("did"))

        metadata = DIDDocumentMetadata.from_dict(d.pop("metadata"))

        did_response = cls(
            did=did,
            metadata=metadata,
        )

        did_response.additional_properties = d
        return did_response

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
