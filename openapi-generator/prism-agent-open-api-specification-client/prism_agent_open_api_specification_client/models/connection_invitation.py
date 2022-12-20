from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ConnectionInvitation")


@attr.s(auto_attribs=True)
class ConnectionInvitation:
    """
    Attributes:
        id (str): The invitation identifier used as parent thread ID (pthid) for the response message that follows.
            Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (str): The DIDComm Message Type URI (MTURI) the invitation message coplies with. Example:
            https://didcomm.org/out-of-band/2.0/invitation.
        from_ (str): The DID representing the sender to be used by recipients for future interactions. Example:
            did:prism:1234457.
        invitation_url (str): The invitation message encoded as a URL. Example: https://domain.com/path?_oob=eyJAaWQiOiI
            zZmE4NWY2NC01NzE3LTQ1NjItYjNmYy0yYzk2M2Y2NmFmYTYiLCJAdHlwZSI6Imh0dHBzOi8vZGlkY29tbS5vcmcvbXktZmFtaWx5LzEuMC9teS1
            tZXNzYWdlLXR5cGUiLCJkaWQiOiJXZ1d4cXp0ck5vb0c5MlJYdnhTVFd2IiwiaW1hZ2VVcmwiOiJodHRwOi8vMTkyLjE2OC41Ni4xMDEvaW1nL2x
            vZ28uanBnIiwibGFiZWwiOiJCb2IiLCJyZWNpcGllbnRLZXlzIjpbIkgzQzJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVB
            WIl0sInJvdXRpbmdLZXlzIjpbIkgzQzJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInNlcnZpY2VFbmRwb2ludCI
            6Imh0dHA6Ly8xOTIuMTY4LjU2LjEwMTo4MDIwIn0=.
    """

    id: str
    type: str
    from_: str
    invitation_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        from_ = self.from_
        invitation_url = self.invitation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "from": from_,
                "invitationUrl": invitation_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        from_ = d.pop("from")

        invitation_url = d.pop("invitationUrl")

        connection_invitation = cls(
            id=id,
            type=type,
            from_=from_,
            invitation_url=invitation_url,
        )

        connection_invitation.additional_properties = d
        return connection_invitation

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
