from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.request_presentation_action import RequestPresentationAction
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Dict[str, Any]:
    url = "{}/present-proof/presentations/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Response[Union[Any, ErrorResponse]]:
    """
    Args:
        id (str):
        json_body (RequestPresentationAction): Actions on presetations (to update) Example:
            {'action': 'request-accept', 'proofId': ['proofId', 'proofId']}.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Optional[Union[Any, ErrorResponse]]:
    """
    Args:
        id (str):
        json_body (RequestPresentationAction): Actions on presetations (to update) Example:
            {'action': 'request-accept', 'proofId': ['proofId', 'proofId']}.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Response[Union[Any, ErrorResponse]]:
    """
    Args:
        id (str):
        json_body (RequestPresentationAction): Actions on presetations (to update) Example:
            {'action': 'request-accept', 'proofId': ['proofId', 'proofId']}.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Optional[Union[Any, ErrorResponse]]:
    """
    Args:
        id (str):
        json_body (RequestPresentationAction): Actions on presetations (to update) Example:
            {'action': 'request-accept', 'proofId': ['proofId', 'proofId']}.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
