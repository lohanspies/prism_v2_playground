from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.public_key_jwk import PublicKeyJwk


T = TypeVar("T", bound="VerificationMethod")


@attr.s(auto_attribs=True)
class VerificationMethod:
    """A cryptographic public key expressed in the DID document.
    https://www.w3.org/TR/did-core/#verification-methods

        Example:
            {'controller': 'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk':
                {'kty': 'EC', 'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
                'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
                'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
                'EcdsaSecp256k1VerificationKey2019'}

        Attributes:
            id (str):  Example: did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1.
            type (str):  Example: EcdsaSecp256k1VerificationKey2019.
            controller (str):  Example: did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff.
            public_key_jwk (PublicKeyJwk):  Example: {'kty': 'EC', 'crv': 'secp256k1', 'x':
                '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}.
    """

    id: str
    type: str
    controller: str
    public_key_jwk: "PublicKeyJwk"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        controller = self.controller
        public_key_jwk = self.public_key_jwk.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "controller": controller,
                "publicKeyJwk": public_key_jwk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.public_key_jwk import PublicKeyJwk

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        controller = d.pop("controller")

        public_key_jwk = PublicKeyJwk.from_dict(d.pop("publicKeyJwk"))

        verification_method = cls(
            id=id,
            type=type,
            controller=controller,
            public_key_jwk=public_key_jwk,
        )

        verification_method.additional_properties = d
        return verification_method

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
