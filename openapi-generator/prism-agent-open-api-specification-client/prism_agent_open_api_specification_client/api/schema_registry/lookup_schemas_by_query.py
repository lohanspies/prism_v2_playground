from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.internal_server_error import InternalServerError
from ...models.verifiable_credential_schema_page import VerifiableCredentialSchemaPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    author: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/schema-registry/schemas".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["author"] = author

    params["name"] = name

    params["tags"] = tags

    params["offset"] = offset

    params["limit"] = limit

    params["order"] = order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[InternalServerError, VerifiableCredentialSchemaPage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VerifiableCredentialSchemaPage.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[InternalServerError, VerifiableCredentialSchemaPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    author: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Response[Union[InternalServerError, VerifiableCredentialSchemaPage]]:
    """Lookup schemas by indexed fields

     Lookup schemas by `author`, `name`, `tags` parameters and control the pagination by `offset` and
    `limit` parameters

    Args:
        author (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        tags (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchemaPage]]
    """

    kwargs = _get_kwargs(
        client=client,
        author=author,
        name=name,
        tags=tags,
        offset=offset,
        limit=limit,
        order=order,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    author: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Optional[Union[InternalServerError, VerifiableCredentialSchemaPage]]:
    """Lookup schemas by indexed fields

     Lookup schemas by `author`, `name`, `tags` parameters and control the pagination by `offset` and
    `limit` parameters

    Args:
        author (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        tags (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchemaPage]]
    """

    return sync_detailed(
        client=client,
        author=author,
        name=name,
        tags=tags,
        offset=offset,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    author: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Response[Union[InternalServerError, VerifiableCredentialSchemaPage]]:
    """Lookup schemas by indexed fields

     Lookup schemas by `author`, `name`, `tags` parameters and control the pagination by `offset` and
    `limit` parameters

    Args:
        author (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        tags (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchemaPage]]
    """

    kwargs = _get_kwargs(
        client=client,
        author=author,
        name=name,
        tags=tags,
        offset=offset,
        limit=limit,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    author: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Optional[Union[InternalServerError, VerifiableCredentialSchemaPage]]:
    """Lookup schemas by indexed fields

     Lookup schemas by `author`, `name`, `tags` parameters and control the pagination by `offset` and
    `limit` parameters

    Args:
        author (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        tags (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchemaPage]]
    """

    return (
        await asyncio_detailed(
            client=client,
            author=author,
            name=name,
            tags=tags,
            offset=offset,
            limit=limit,
            order=order,
        )
    ).parsed
