from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicKeyJwk")


@attr.s(auto_attribs=True)
class PublicKeyJwk:
    """
    Example:
        {'kty': 'EC', 'crv': 'secp256k1', 'kid': '_TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw', 'x':
            '38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8', 'y': 'nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4'}

    Attributes:
        kty (str):  Example: EC.
        crv (Union[Unset, str]):  Example: secp256k1.
        x (Union[Unset, str]):  Example: 38M1FDts7Oea7urmseiugGW7tWc3mLpJh6rKe7xINZ8.
        y (Union[Unset, str]):  Example: nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4.
        kid (Union[Unset, str]):  Example: _TKzHv2jFIyvdTGF1Dsgwngfdg3SH6TpDv0Ta1aOEkw.
    """

    kty: str
    crv: Union[Unset, str] = UNSET
    x: Union[Unset, str] = UNSET
    y: Union[Unset, str] = UNSET
    kid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kty = self.kty
        crv = self.crv
        x = self.x
        y = self.y
        kid = self.kid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kty": kty,
            }
        )
        if crv is not UNSET:
            field_dict["crv"] = crv
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if kid is not UNSET:
            field_dict["kid"] = kid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kty = d.pop("kty")

        crv = d.pop("crv", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        kid = d.pop("kid", UNSET)

        public_key_jwk = cls(
            kty=kty,
            crv=crv,
            x=x,
            y=y,
            kid=kid,
        )

        public_key_jwk.additional_properties = d
        return public_key_jwk

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
