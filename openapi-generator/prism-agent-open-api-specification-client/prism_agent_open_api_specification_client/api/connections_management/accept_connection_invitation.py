from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.accept_connection_invitation_request import AcceptConnectionInvitationRequest
from ...models.connection import Connection
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AcceptConnectionInvitationRequest,
) -> Dict[str, Any]:
    url = "{}/connection-invitations".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Connection, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Connection.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Connection, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AcceptConnectionInvitationRequest,
) -> Response[Union[Connection, ErrorResponse]]:
    """Accepts externally received invitation.

     Creates new connection state record in `pending` state. It is assumed that application would first
    decode and validate the invitation. When it is accepted in the application side, it should be
    submitted in raw format to this API.

    Args:
        json_body (AcceptConnectionInvitationRequest):  Example: {'invitation': 'eyJAaWQiOiIzZmE4N
            WY2NC01NzE3LTQ1NjItYjNmYy0yYzk2M2Y2NmFmYTYiLCJAdHlwZSI6Imh0dHBzOi8vZGlkY29tbS5vcmcvbXktZmF
            taWx5LzEuMC9teS1tZXNzYWdlLXR5cGUiLCJkaWQiOiJXZ1d4cXp0ck5vb0c5MlJYdnhTVFd2IiwiaW1hZ2VVcmwiO
            iJodHRwOi8vMTkyLjE2OC41Ni4xMDEvaW1nL2xvZ28uanBnIiwibGFiZWwiOiJCb2IiLCJyZWNpcGllbnRLZXlzIjp
            bIkgzQzJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInJvdXRpbmdLZXlzIjpbIkgzQ
            zJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInNlcnZpY2VFbmRwb2ludCI6Imh0dHA
            6Ly8xOTIuMTY4LjU2LjEwMTo4MDIwIn0='}.

    Returns:
        Response[Union[Connection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: AcceptConnectionInvitationRequest,
) -> Optional[Union[Connection, ErrorResponse]]:
    """Accepts externally received invitation.

     Creates new connection state record in `pending` state. It is assumed that application would first
    decode and validate the invitation. When it is accepted in the application side, it should be
    submitted in raw format to this API.

    Args:
        json_body (AcceptConnectionInvitationRequest):  Example: {'invitation': 'eyJAaWQiOiIzZmE4N
            WY2NC01NzE3LTQ1NjItYjNmYy0yYzk2M2Y2NmFmYTYiLCJAdHlwZSI6Imh0dHBzOi8vZGlkY29tbS5vcmcvbXktZmF
            taWx5LzEuMC9teS1tZXNzYWdlLXR5cGUiLCJkaWQiOiJXZ1d4cXp0ck5vb0c5MlJYdnhTVFd2IiwiaW1hZ2VVcmwiO
            iJodHRwOi8vMTkyLjE2OC41Ni4xMDEvaW1nL2xvZ28uanBnIiwibGFiZWwiOiJCb2IiLCJyZWNpcGllbnRLZXlzIjp
            bIkgzQzJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInJvdXRpbmdLZXlzIjpbIkgzQ
            zJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInNlcnZpY2VFbmRwb2ludCI6Imh0dHA
            6Ly8xOTIuMTY4LjU2LjEwMTo4MDIwIn0='}.

    Returns:
        Response[Union[Connection, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AcceptConnectionInvitationRequest,
) -> Response[Union[Connection, ErrorResponse]]:
    """Accepts externally received invitation.

     Creates new connection state record in `pending` state. It is assumed that application would first
    decode and validate the invitation. When it is accepted in the application side, it should be
    submitted in raw format to this API.

    Args:
        json_body (AcceptConnectionInvitationRequest):  Example: {'invitation': 'eyJAaWQiOiIzZmE4N
            WY2NC01NzE3LTQ1NjItYjNmYy0yYzk2M2Y2NmFmYTYiLCJAdHlwZSI6Imh0dHBzOi8vZGlkY29tbS5vcmcvbXktZmF
            taWx5LzEuMC9teS1tZXNzYWdlLXR5cGUiLCJkaWQiOiJXZ1d4cXp0ck5vb0c5MlJYdnhTVFd2IiwiaW1hZ2VVcmwiO
            iJodHRwOi8vMTkyLjE2OC41Ni4xMDEvaW1nL2xvZ28uanBnIiwibGFiZWwiOiJCb2IiLCJyZWNpcGllbnRLZXlzIjp
            bIkgzQzJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInJvdXRpbmdLZXlzIjpbIkgzQ
            zJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInNlcnZpY2VFbmRwb2ludCI6Imh0dHA
            6Ly8xOTIuMTY4LjU2LjEwMTo4MDIwIn0='}.

    Returns:
        Response[Union[Connection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: AcceptConnectionInvitationRequest,
) -> Optional[Union[Connection, ErrorResponse]]:
    """Accepts externally received invitation.

     Creates new connection state record in `pending` state. It is assumed that application would first
    decode and validate the invitation. When it is accepted in the application side, it should be
    submitted in raw format to this API.

    Args:
        json_body (AcceptConnectionInvitationRequest):  Example: {'invitation': 'eyJAaWQiOiIzZmE4N
            WY2NC01NzE3LTQ1NjItYjNmYy0yYzk2M2Y2NmFmYTYiLCJAdHlwZSI6Imh0dHBzOi8vZGlkY29tbS5vcmcvbXktZmF
            taWx5LzEuMC9teS1tZXNzYWdlLXR5cGUiLCJkaWQiOiJXZ1d4cXp0ck5vb0c5MlJYdnhTVFd2IiwiaW1hZ2VVcmwiO
            iJodHRwOi8vMTkyLjE2OC41Ni4xMDEvaW1nL2xvZ28uanBnIiwibGFiZWwiOiJCb2IiLCJyZWNpcGllbnRLZXlzIjp
            bIkgzQzJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInJvdXRpbmdLZXlzIjpbIkgzQ
            zJBVnZMTXY2Z21NTmFtM3VWQWpacGZrY0pDd0R3blpuNnozd1htcVBWIl0sInNlcnZpY2VFbmRwb2ludCI6Imh0dHA
            6Ly8xOTIuMTY4LjU2LjEwMTo4MDIwIn0='}.

    Returns:
        Response[Union[Connection, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
