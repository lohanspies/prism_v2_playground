import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.connection_all_of_role import ConnectionAllOfRole
from ..models.connection_all_of_state import ConnectionAllOfState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_invitation import ConnectionInvitation


T = TypeVar("T", bound="Connection")


@attr.s(auto_attribs=True)
class Connection:
    """A connection record.

    Attributes:
        self_ (str): The reference to the connection resource. Example: https://atala-prism-
            products.io/connections/ABCD-1234.
        kind (str): The type of object returned. In this case a `Connection`. Example: Connection.
        connection_id (str): The unique identifier of the connection. Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        state (ConnectionAllOfState): The current state of the connection protocol execution.
        created_at (datetime.datetime): The date and time the connection record was created. Example: 2021-10-31
            09:22:23+00:00.
        role (ConnectionAllOfRole): The role played by the Prism agent in the connection flow.
        invitation (ConnectionInvitation): A connection invitation.
        label (Union[Unset, str]): A human readable alias for the connection. Example: Peter.
        my_did (Union[Unset, str]): The DID representing me as the inviter or invitee in this specific connection.
            Example: did:peer:12345.
        their_did (Union[Unset, str]): The DID representing the other peer as the an inviter or invitee in this specific
            connection. Example: did:peer:67890.
        updated_at (Union[Unset, datetime.datetime]): The date and time the connection record was last updated. Example:
            2021-12-31 13:59:59+00:00.
    """

    self_: str
    kind: str
    connection_id: str
    state: ConnectionAllOfState
    created_at: datetime.datetime
    role: ConnectionAllOfRole
    invitation: "ConnectionInvitation"
    label: Union[Unset, str] = UNSET
    my_did: Union[Unset, str] = UNSET
    their_did: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_
        kind = self.kind
        connection_id = self.connection_id
        state = self.state.value

        created_at = self.created_at.isoformat()

        role = self.role.value

        invitation = self.invitation.to_dict()

        label = self.label
        my_did = self.my_did
        their_did = self.their_did
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "kind": kind,
                "connectionId": connection_id,
                "state": state,
                "createdAt": created_at,
                "role": role,
                "invitation": invitation,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if my_did is not UNSET:
            field_dict["myDid"] = my_did
        if their_did is not UNSET:
            field_dict["theirDid"] = their_did
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connection_invitation import ConnectionInvitation

        d = src_dict.copy()
        self_ = d.pop("self")

        kind = d.pop("kind")

        connection_id = d.pop("connectionId")

        state = ConnectionAllOfState(d.pop("state"))

        created_at = isoparse(d.pop("createdAt"))

        role = ConnectionAllOfRole(d.pop("role"))

        invitation = ConnectionInvitation.from_dict(d.pop("invitation"))

        label = d.pop("label", UNSET)

        my_did = d.pop("myDid", UNSET)

        their_did = d.pop("theirDid", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        connection = cls(
            self_=self_,
            kind=kind,
            connection_id=connection_id,
            state=state,
            created_at=created_at,
            role=role,
            invitation=invitation,
            label=label,
            my_did=my_did,
            their_did=their_did,
            updated_at=updated_at,
        )

        connection.additional_properties = d
        return connection

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
