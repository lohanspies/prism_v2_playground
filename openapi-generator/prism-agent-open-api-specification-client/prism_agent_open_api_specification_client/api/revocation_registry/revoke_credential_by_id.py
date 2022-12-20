from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.w3c_credential_revocation_request import W3CCredentialRevocationRequest
from ...models.w3c_credential_revocation_response import W3CCredentialRevocationResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: W3CCredentialRevocationRequest,
) -> Dict[str, Any]:
    url = "{}/revocation-registry/revoke".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[W3CCredentialRevocationResponse]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = W3CCredentialRevocationResponse.from_dict(response.json())

        return response_202
    return None


def _build_response(*, response: httpx.Response) -> Response[W3CCredentialRevocationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: W3CCredentialRevocationRequest,
) -> Response[W3CCredentialRevocationResponse]:
    """Revoke credential by id

     Revoke credential by id

    Args:
        json_body (W3CCredentialRevocationRequest): Credential revocation request. Contain
            credential id and other information required for revocation Example: {'credentialId':
            'abcde-12345'}.

    Returns:
        Response[W3CCredentialRevocationResponse]
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
    json_body: W3CCredentialRevocationRequest,
) -> Optional[W3CCredentialRevocationResponse]:
    """Revoke credential by id

     Revoke credential by id

    Args:
        json_body (W3CCredentialRevocationRequest): Credential revocation request. Contain
            credential id and other information required for revocation Example: {'credentialId':
            'abcde-12345'}.

    Returns:
        Response[W3CCredentialRevocationResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: W3CCredentialRevocationRequest,
) -> Response[W3CCredentialRevocationResponse]:
    """Revoke credential by id

     Revoke credential by id

    Args:
        json_body (W3CCredentialRevocationRequest): Credential revocation request. Contain
            credential id and other information required for revocation Example: {'credentialId':
            'abcde-12345'}.

    Returns:
        Response[W3CCredentialRevocationResponse]
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
    json_body: W3CCredentialRevocationRequest,
) -> Optional[W3CCredentialRevocationResponse]:
    """Revoke credential by id

     Revoke credential by id

    Args:
        json_body (W3CCredentialRevocationRequest): Credential revocation request. Contain
            credential id and other information required for revocation Example: {'credentialId':
            'abcde-12345'}.

    Returns:
        Response[W3CCredentialRevocationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
