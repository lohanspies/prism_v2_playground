from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.create_managed_did_request import CreateManagedDidRequest
from ...models.create_managed_did_response import CreateManagedDIDResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateManagedDidRequest,
) -> Dict[str, Any]:
    url = "{}/did-registrar/dids".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[CreateManagedDIDResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateManagedDIDResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CreateManagedDIDResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateManagedDidRequest,
) -> Response[Union[CreateManagedDIDResponse, ErrorResponse]]:
    """Create unpublished DID and store it in PrismAgent's wallet

     Create unpublished DID and store it inside PrismAgent's wallet. The private keys of the DID is
    managed by PrismAgent. The DID can later be published to blockchain using publications endpoint.

    Args:
        json_body (CreateManagedDidRequest):  Example: {'documentTemplate': {'publicKeys':
            [{'purpose': 'authentication', 'id': 'key1'}, {'purpose': 'authentication', 'id':
            'key1'}], 'services': [{'id': 'service1', 'serviceEndpoint': ['https://bar.example.com',
            'https://bar.example.com'], 'type': 'MediatorService'}, {'id': 'service1',
            'serviceEndpoint': ['https://bar.example.com', 'https://bar.example.com'], 'type':
            'MediatorService'}]}}.

    Returns:
        Response[Union[CreateManagedDIDResponse, ErrorResponse]]
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
    json_body: CreateManagedDidRequest,
) -> Optional[Union[CreateManagedDIDResponse, ErrorResponse]]:
    """Create unpublished DID and store it in PrismAgent's wallet

     Create unpublished DID and store it inside PrismAgent's wallet. The private keys of the DID is
    managed by PrismAgent. The DID can later be published to blockchain using publications endpoint.

    Args:
        json_body (CreateManagedDidRequest):  Example: {'documentTemplate': {'publicKeys':
            [{'purpose': 'authentication', 'id': 'key1'}, {'purpose': 'authentication', 'id':
            'key1'}], 'services': [{'id': 'service1', 'serviceEndpoint': ['https://bar.example.com',
            'https://bar.example.com'], 'type': 'MediatorService'}, {'id': 'service1',
            'serviceEndpoint': ['https://bar.example.com', 'https://bar.example.com'], 'type':
            'MediatorService'}]}}.

    Returns:
        Response[Union[CreateManagedDIDResponse, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateManagedDidRequest,
) -> Response[Union[CreateManagedDIDResponse, ErrorResponse]]:
    """Create unpublished DID and store it in PrismAgent's wallet

     Create unpublished DID and store it inside PrismAgent's wallet. The private keys of the DID is
    managed by PrismAgent. The DID can later be published to blockchain using publications endpoint.

    Args:
        json_body (CreateManagedDidRequest):  Example: {'documentTemplate': {'publicKeys':
            [{'purpose': 'authentication', 'id': 'key1'}, {'purpose': 'authentication', 'id':
            'key1'}], 'services': [{'id': 'service1', 'serviceEndpoint': ['https://bar.example.com',
            'https://bar.example.com'], 'type': 'MediatorService'}, {'id': 'service1',
            'serviceEndpoint': ['https://bar.example.com', 'https://bar.example.com'], 'type':
            'MediatorService'}]}}.

    Returns:
        Response[Union[CreateManagedDIDResponse, ErrorResponse]]
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
    json_body: CreateManagedDidRequest,
) -> Optional[Union[CreateManagedDIDResponse, ErrorResponse]]:
    """Create unpublished DID and store it in PrismAgent's wallet

     Create unpublished DID and store it inside PrismAgent's wallet. The private keys of the DID is
    managed by PrismAgent. The DID can later be published to blockchain using publications endpoint.

    Args:
        json_body (CreateManagedDidRequest):  Example: {'documentTemplate': {'publicKeys':
            [{'purpose': 'authentication', 'id': 'key1'}, {'purpose': 'authentication', 'id':
            'key1'}], 'services': [{'id': 'service1', 'serviceEndpoint': ['https://bar.example.com',
            'https://bar.example.com'], 'type': 'MediatorService'}, {'id': 'service1',
            'serviceEndpoint': ['https://bar.example.com', 'https://bar.example.com'], 'type':
            'MediatorService'}]}}.

    Returns:
        Response[Union[CreateManagedDIDResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
