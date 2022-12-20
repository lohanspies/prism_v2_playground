from http import HTTPStatus
from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/connections/{connectionId}".format(client.base_url, connectionId=connection_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Deletes existing connection record.

     Just deletes connection state in the Agent, it does not include notifing other party that connection
    is deleted. We should consider this feature for the future. If additional action is attempted over
    deleted connection, it should thow error (no matter which side deleted connection).

    Args:
        connection_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Deletes existing connection record.

     Just deletes connection state in the Agent, it does not include notifing other party that connection
    is deleted. We should consider this feature for the future. If additional action is attempted over
    deleted connection, it should thow error (no matter which side deleted connection).

    Args:
        connection_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
