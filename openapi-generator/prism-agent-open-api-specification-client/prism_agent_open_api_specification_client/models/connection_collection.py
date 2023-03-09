from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.connection import Connection


T = TypeVar("T", bound="ConnectionCollection")


@attr.s(auto_attribs=True)
class ConnectionCollection:
    """A collection of connection records.

    Example:
        {'contents': [None, None], 'kind': 'Collection', 'self': 'https://atala-prism-products.io/connections'}

    Attributes:
        self_ (str): The reference to the connection collection itself. Example: https://atala-prism-
            products.io/connections.
        kind (str): The type of object returned. In this case a `Collection`. Example: Collection.
        contents (List['Connection']): The array containing the list of connection records.
    """

    self_: str
    kind: str
    contents: List["Connection"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_
        kind = self.kind
        contents = []
        for contents_item_data in self.contents:
            contents_item = contents_item_data.to_dict()

            contents.append(contents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "kind": kind,
                "contents": contents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connection import Connection

        d = src_dict.copy()
        self_ = d.pop("self")

        kind = d.pop("kind")

        contents = []
        _contents = d.pop("contents")
        for contents_item_data in _contents:
            contents_item = Connection.from_dict(contents_item_data)

            contents.append(contents_item)

        connection_collection = cls(
            self_=self_,
            kind=kind,
            contents=contents,
        )

        connection_collection.additional_properties = d
        return connection_collection

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
