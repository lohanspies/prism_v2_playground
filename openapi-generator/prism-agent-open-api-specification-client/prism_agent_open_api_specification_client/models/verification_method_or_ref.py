from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.verification_method_or_ref_type import VerificationMethodOrRefType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verification_method import VerificationMethod


T = TypeVar("T", bound="VerificationMethodOrRef")


@attr.s(auto_attribs=True)
class VerificationMethodOrRef:
    """An embedded verificationMethod as JSON or a referenced key as a URI.
    Referenced key and embedded key are mutually exclusive.
    If the type is EMBEDDED, `uri` field must be present.
    Otherwise `verificationMethod` field must be present.

        Example:
            {'type': 'EMBEDDED', 'verificationMethod': {'controller':
                'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff', 'publicKeyJwk': {'kty': 'EC',
                'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
                'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
                'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
                'EcdsaSecp256k1VerificationKey2019'}, 'uri':
                'did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1'}

        Attributes:
            type (VerificationMethodOrRefType):  Example: EMBEDDED.
            uri (Union[Unset, str]):  Example:
                did:prism:c7bd808e8e135236d7262ecf5e639b8f9d22bd886f59a4e6c909486846ca8319#key-1.
            verification_method (Union[Unset, VerificationMethod]): A cryptographic public key expressed in the DID
                document.
                https://www.w3.org/TR/did-core/#verification-methods
                 Example: {'controller': 'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff',
                'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
                'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id':
                'did:prism:4a5b5cf0a513e83b598bbea25cd6196746747f361a73ef77068268bc9bd732ff#key-1', 'type':
                'EcdsaSecp256k1VerificationKey2019'}.
    """

    type: VerificationMethodOrRefType
    uri: Union[Unset, str] = UNSET
    verification_method: Union[Unset, "VerificationMethod"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        uri = self.uri
        verification_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verification_method, Unset):
            verification_method = self.verification_method.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if uri is not UNSET:
            field_dict["uri"] = uri
        if verification_method is not UNSET:
            field_dict["verificationMethod"] = verification_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.verification_method import VerificationMethod

        d = src_dict.copy()
        type = VerificationMethodOrRefType(d.pop("type"))

        uri = d.pop("uri", UNSET)

        _verification_method = d.pop("verificationMethod", UNSET)
        verification_method: Union[Unset, VerificationMethod]
        if isinstance(_verification_method, Unset):
            verification_method = UNSET
        else:
            verification_method = VerificationMethod.from_dict(_verification_method)

        verification_method_or_ref = cls(
            type=type,
            uri=uri,
            verification_method=verification_method,
        )

        verification_method_or_ref.additional_properties = d
        return verification_method_or_ref

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
