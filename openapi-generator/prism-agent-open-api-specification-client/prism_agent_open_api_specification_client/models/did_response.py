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
        {'metadata': {'canonicalId': 'canonicalId', 'deactivated': True}, 'did': {'assertionMethod': [{'type':
            'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'service': [{'id': 'service-1',
            'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type': 'LinkedDomains'}, {'id':
            'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type':
            'LinkedDomains'}], 'keyAgreement': [{'type': 'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'capabilityDelegation':
            [{'type': 'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'verificationMethod':
            [{'controller': 'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk':
            {'kty': 'EC', 'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}], 'capabilityInvocation': [{'type': 'EMBEDDED', 'verificationMethod':
            {'controller': 'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk':
            {'kty': 'EC', 'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'authentication':
            [{'type': 'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}]}}

    Attributes:
        did (DID): A Prism DID document data model capable of being transformed into W3C compliant representation.
             Example: {'assertionMethod': [{'type': 'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'service': [{'id': 'service-1',
            'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type': 'LinkedDomains'}, {'id':
            'service-1', 'serviceEndpoint': ['https://bar.example.com/', 'https://bar.example.com/'], 'type':
            'LinkedDomains'}], 'keyAgreement': [{'type': 'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'capabilityDelegation':
            [{'type': 'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'verificationMethod':
            [{'controller': 'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk':
            {'kty': 'EC', 'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}], 'capabilityInvocation': [{'type': 'EMBEDDED', 'verificationMethod':
            {'controller': 'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk':
            {'kty': 'EC', 'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}], 'authentication':
            [{'type': 'EMBEDDED', 'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}, {'type': 'EMBEDDED',
            'verificationMethod': {'controller':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
            'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
            'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, 'uri':
            'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}]}.
        metadata (DIDDocumentMetadata): [DID document metadata](https://www.w3.org/TR/did-core/#did-document-metadata)
             Example: {'canonicalId': 'canonicalId', 'deactivated': True}.
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
