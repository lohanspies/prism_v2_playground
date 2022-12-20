from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.connection import Connection
from ...models.error_response import ErrorResponse
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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Connection, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Connection.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Connection, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Client,
) -> Response[Union[Connection, ErrorResponse]]:
    """Returns an existing connection record by id.

    Args:
        connection_id (str):

    Returns:
        Response[Union[Connection, ErrorResponse]]
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


def sync(
    connection_id: str,
    *,
    client: Client,
) -> Optional[Union[Connection, ErrorResponse]]:
    """Returns an existing connection record by id.

    Args:
        connection_id (str):

    Returns:
        Response[Union[Connection, ErrorResponse]]
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Client,
) -> Response[Union[Connection, ErrorResponse]]:
    """Returns an existing connection record by id.

    Args:
        connection_id (str):

    Returns:
        Response[Union[Connection, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    connection_id: str,
    *,
    client: Client,
) -> Optional[Union[Connection, ErrorResponse]]:
    """Returns an existing connection record by id.

    Args:
        connection_id (str):

    Returns:
        Response[Union[Connection, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
        )
    ).parsed
