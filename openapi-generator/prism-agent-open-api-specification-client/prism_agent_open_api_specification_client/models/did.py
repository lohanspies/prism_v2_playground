from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service import Service
    from ..models.verification_method import VerificationMethod


T = TypeVar("T", bound="DID")


@attr.s(auto_attribs=True)
class DID:
    """
    Example:
        {'assertionMethod': [{'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv': 'secp256k1', 'kid':
            '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x': '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y':
            'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}, 'id': 'did:prism:123#key-1', 'type':
            'EcdsaSecp256k1VerificationKey2019'}, {'controller': 'did:prism:456', 'publicKeyJwk': {'kty': 'EC', 'crv':
            'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
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
            'did:prism:123#key-1', 'type': 'EcdsaSecp256k1VerificationKey2019'}]}

    Attributes:
        id (str):  Example: did:prism:mainnet:123.
        controller (Union[Unset, str]):  Example: did:prism:mainnet:456.
        verification_method (Union[Unset, List['VerificationMethod']]):
        authentication (Union[Unset, List['VerificationMethod']]):
        assertion_method (Union[Unset, List['VerificationMethod']]):
        key_agreement (Union[Unset, List['VerificationMethod']]):
        capability_invocation (Union[Unset, List['VerificationMethod']]):
        service (Union[Unset, List['Service']]):
    """

    id: str
    controller: Union[Unset, str] = UNSET
    verification_method: Union[Unset, List["VerificationMethod"]] = UNSET
    authentication: Union[Unset, List["VerificationMethod"]] = UNSET
    assertion_method: Union[Unset, List["VerificationMethod"]] = UNSET
    key_agreement: Union[Unset, List["VerificationMethod"]] = UNSET
    capability_invocation: Union[Unset, List["VerificationMethod"]] = UNSET
    service: Union[Unset, List["Service"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        controller = self.controller
        verification_method: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.verification_method, Unset):
            verification_method = []
            for verification_method_item_data in self.verification_method:
                verification_method_item = verification_method_item_data.to_dict()

                verification_method.append(verification_method_item)

        authentication: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = []
            for authentication_item_data in self.authentication:
                authentication_item = authentication_item_data.to_dict()

                authentication.append(authentication_item)

        assertion_method: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assertion_method, Unset):
            assertion_method = []
            for assertion_method_item_data in self.assertion_method:
                assertion_method_item = assertion_method_item_data.to_dict()

                assertion_method.append(assertion_method_item)

        key_agreement: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.key_agreement, Unset):
            key_agreement = []
            for key_agreement_item_data in self.key_agreement:
                key_agreement_item = key_agreement_item_data.to_dict()

                key_agreement.append(key_agreement_item)

        capability_invocation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.capability_invocation, Unset):
            capability_invocation = []
            for capability_invocation_item_data in self.capability_invocation:
                capability_invocation_item = capability_invocation_item_data.to_dict()

                capability_invocation.append(capability_invocation_item)

        service: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service, Unset):
            service = []
            for service_item_data in self.service:
                service_item = service_item_data.to_dict()

                service.append(service_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if controller is not UNSET:
            field_dict["controller"] = controller
        if verification_method is not UNSET:
            field_dict["verificationMethod"] = verification_method
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if assertion_method is not UNSET:
            field_dict["assertionMethod"] = assertion_method
        if key_agreement is not UNSET:
            field_dict["keyAgreement"] = key_agreement
        if capability_invocation is not UNSET:
            field_dict["capabilityInvocation"] = capability_invocation
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service import Service
        from ..models.verification_method import VerificationMethod

        d = src_dict.copy()
        id = d.pop("id")

        controller = d.pop("controller", UNSET)

        verification_method = []
        _verification_method = d.pop("verificationMethod", UNSET)
        for verification_method_item_data in _verification_method or []:
            verification_method_item = VerificationMethod.from_dict(verification_method_item_data)

            verification_method.append(verification_method_item)

        authentication = []
        _authentication = d.pop("authentication", UNSET)
        for authentication_item_data in _authentication or []:
            authentication_item = VerificationMethod.from_dict(authentication_item_data)

            authentication.append(authentication_item)

        assertion_method = []
        _assertion_method = d.pop("assertionMethod", UNSET)
        for assertion_method_item_data in _assertion_method or []:
            assertion_method_item = VerificationMethod.from_dict(assertion_method_item_data)

            assertion_method.append(assertion_method_item)

        key_agreement = []
        _key_agreement = d.pop("keyAgreement", UNSET)
        for key_agreement_item_data in _key_agreement or []:
            key_agreement_item = VerificationMethod.from_dict(key_agreement_item_data)

            key_agreement.append(key_agreement_item)

        capability_invocation = []
        _capability_invocation = d.pop("capabilityInvocation", UNSET)
        for capability_invocation_item_data in _capability_invocation or []:
            capability_invocation_item = VerificationMethod.from_dict(capability_invocation_item_data)

            capability_invocation.append(capability_invocation_item)

        service = []
        _service = d.pop("service", UNSET)
        for service_item_data in _service or []:
            service_item = Service.from_dict(service_item_data)

            service.append(service_item)

        did = cls(
            id=id,
            controller=controller,
            verification_method=verification_method,
            authentication=authentication,
            assertion_method=assertion_method,
            key_agreement=key_agreement,
            capability_invocation=capability_invocation,
            service=service,
        )

        did.additional_properties = d
        return did

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
