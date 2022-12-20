from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.did_response import DIDResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    did_ref: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/dids/{didRef}".format(client.base_url, didRef=did_ref)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DIDResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DIDResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DIDResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    did_ref: str,
    *,
    client: Client,
) -> Response[Union[DIDResponse, ErrorResponse]]:
    """Resolve Prism DID

     Resolve Prism DID

    Args:
        did_ref (str):

    Returns:
        Response[Union[DIDResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        did_ref=did_ref,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    did_ref: str,
    *,
    client: Client,
) -> Optional[Union[DIDResponse, ErrorResponse]]:
    """Resolve Prism DID

     Resolve Prism DID

    Args:
        did_ref (str):

    Returns:
        Response[Union[DIDResponse, ErrorResponse]]
    """

    return sync_detailed(
        did_ref=did_ref,
        client=client,
    ).parsed


async def asyncio_detailed(
    did_ref: str,
    *,
    client: Client,
) -> Response[Union[DIDResponse, ErrorResponse]]:
    """Resolve Prism DID

     Resolve Prism DID

    Args:
        did_ref (str):

    Returns:
        Response[Union[DIDResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        did_ref=did_ref,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    did_ref: str,
    *,
    client: Client,
) -> Optional[Union[DIDResponse, ErrorResponse]]:
    """Resolve Prism DID

     Resolve Prism DID

    Args:
        did_ref (str):

    Returns:
        Response[Union[DIDResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            did_ref=did_ref,
            client=client,
        )
    ).parsed
