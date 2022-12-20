from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.not_found import NotFound
from ...models.verifiable_credential_schema import VerifiableCredentialSchema
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/schema-registry/schemas/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[NotFound, VerifiableCredentialSchema]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VerifiableCredentialSchema.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[NotFound, VerifiableCredentialSchema]]:
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
) -> Response[Union[NotFound, VerifiableCredentialSchema]]:
    """Fetch the schema from the registry by id

     Fetch the schema by the unique identifier. Verifiable Credential Schema in json format is returned.

    Args:
        id (str):

    Returns:
        Response[Union[NotFound, VerifiableCredentialSchema]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
) -> Optional[Union[NotFound, VerifiableCredentialSchema]]:
    """Fetch the schema from the registry by id

     Fetch the schema by the unique identifier. Verifiable Credential Schema in json format is returned.

    Args:
        id (str):

    Returns:
        Response[Union[NotFound, VerifiableCredentialSchema]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[NotFound, VerifiableCredentialSchema]]:
    """Fetch the schema from the registry by id

     Fetch the schema by the unique identifier. Verifiable Credential Schema in json format is returned.

    Args:
        id (str):

    Returns:
        Response[Union[NotFound, VerifiableCredentialSchema]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[Union[NotFound, VerifiableCredentialSchema]]:
    """Fetch the schema from the registry by id

     Fetch the schema by the unique identifier. Verifiable Credential Schema in json format is returned.

    Args:
        id (str):

    Returns:
        Response[Union[NotFound, VerifiableCredentialSchema]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
