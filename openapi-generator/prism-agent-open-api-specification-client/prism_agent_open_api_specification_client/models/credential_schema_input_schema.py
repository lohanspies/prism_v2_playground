from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CredentialSchemaInputSchema")


@attr.s(auto_attribs=True)
class CredentialSchemaInputSchema:
    """Valid JSON Schema where the Credential Schema data fields are defined
    A piece of Metadata

        Example:
            {'example': {'$id': 'driving-license-1.0', '$schema': 'https://json-schema.org/draft/2020-12/schema',
                'description': 'Driving License', 'type': 'object', 'properties': {'credentialSubject': {'type': 'object',
                'properties': {'emailAddress': {'type': 'string', 'format': 'email'}, 'givenName': {'type': 'string'},
                'familyName': {'type': 'string'}, 'dateOfIssuance': {'type': 'datetime'}, 'drivingLicenseID': {'type':
                'string'}, 'drivingClass': {'type': 'integer'}, 'required': ['emailAddress', 'familyName', 'dateOfIssuance',
                'drivingLicenseID', 'drivingClass'], 'additionalProperties': True}}}}}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credential_schema_input_schema = cls()

        credential_schema_input_schema.additional_properties = d
        return credential_schema_input_schema

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
