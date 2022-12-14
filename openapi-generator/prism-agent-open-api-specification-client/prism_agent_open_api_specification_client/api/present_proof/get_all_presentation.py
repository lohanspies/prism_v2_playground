from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.presentation_status import PresentationStatus
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/present-proof/presentations".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, List["PresentationStatus"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PresentationStatus.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, List["PresentationStatus"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[ErrorResponse, List["PresentationStatus"]]]:
    """
    Returns:
        Response[Union[ErrorResponse, List['PresentationStatus']]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, List["PresentationStatus"]]]:
    """
    Returns:
        Response[Union[ErrorResponse, List['PresentationStatus']]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[ErrorResponse, List["PresentationStatus"]]]:
    """
    Returns:
        Response[Union[ErrorResponse, List['PresentationStatus']]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, List["PresentationStatus"]]]:
    """
    Returns:
        Response[Union[ErrorResponse, List['PresentationStatus']]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
