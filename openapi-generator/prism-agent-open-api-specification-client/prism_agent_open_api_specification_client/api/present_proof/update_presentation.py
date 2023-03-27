from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.request_presentation_action import RequestPresentationAction
from ...types import Response


def _get_kwargs(
    record_id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Dict[str, Any]:
    url = "{}/present-proof/presentations/{recordId}".format(client.base_url, recordId=record_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    record_id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Response[Union[Any, ErrorResponse]]:
    """Updates the proof presentation record matching the unique identifier, with the specific action to
    perform.

     Accept or reject presentation of proof request

    Args:
        record_id (str):
        json_body (RequestPresentationAction): The action to perform on the proof presentation
            record. Example: {'action': 'request-accept', 'proofId':
            ['0d3a0f8d-852e-42d5-a6f8-2281c4be945c', '0d3a0f8d-852e-42d5-a6f8-2281c4be945c']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    record_id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Optional[Union[Any, ErrorResponse]]:
    """Updates the proof presentation record matching the unique identifier, with the specific action to
    perform.

     Accept or reject presentation of proof request

    Args:
        record_id (str):
        json_body (RequestPresentationAction): The action to perform on the proof presentation
            record. Example: {'action': 'request-accept', 'proofId':
            ['0d3a0f8d-852e-42d5-a6f8-2281c4be945c', '0d3a0f8d-852e-42d5-a6f8-2281c4be945c']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    record_id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Response[Union[Any, ErrorResponse]]:
    """Updates the proof presentation record matching the unique identifier, with the specific action to
    perform.

     Accept or reject presentation of proof request

    Args:
        record_id (str):
        json_body (RequestPresentationAction): The action to perform on the proof presentation
            record. Example: {'action': 'request-accept', 'proofId':
            ['0d3a0f8d-852e-42d5-a6f8-2281c4be945c', '0d3a0f8d-852e-42d5-a6f8-2281c4be945c']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    record_id: str,
    *,
    client: Client,
    json_body: RequestPresentationAction,
) -> Optional[Union[Any, ErrorResponse]]:
    """Updates the proof presentation record matching the unique identifier, with the specific action to
    perform.

     Accept or reject presentation of proof request

    Args:
        record_id (str):
        json_body (RequestPresentationAction): The action to perform on the proof presentation
            record. Example: {'action': 'request-accept', 'proofId':
            ['0d3a0f8d-852e-42d5-a6f8-2281c4be945c', '0d3a0f8d-852e-42d5-a6f8-2281c4be945c']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
