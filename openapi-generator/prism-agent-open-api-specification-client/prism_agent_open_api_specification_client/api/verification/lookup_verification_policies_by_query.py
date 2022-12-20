from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request import BadRequest
from ...models.internal_server_error import InternalServerError
from ...models.verification_policy_page import VerificationPolicyPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    issuer_di_ds: Union[Unset, None, str] = UNSET,
    credential_types: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/verification/policies".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params["attributes"] = attributes

    params["issuerDIDs"] = issuer_di_ds

    params["credentialTypes"] = credential_types

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
) -> Optional[Union[BadRequest, InternalServerError, VerificationPolicyPage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VerificationPolicyPage.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[BadRequest, InternalServerError, VerificationPolicyPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    issuer_di_ds: Union[Unset, None, str] = UNSET,
    credential_types: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Response[Union[BadRequest, InternalServerError, VerificationPolicyPage]]:
    """Lookup verification policies by query

     Lookup verification policies by `name`, `attributes`, `issuerDIDs`, and `credentialTypes` and
    control the pagination by `offset` and `limit` parameters

    Args:
        name (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        issuer_di_ds (Union[Unset, None, str]):
        credential_types (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicyPage]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        attributes=attributes,
        issuer_di_ds=issuer_di_ds,
        credential_types=credential_types,
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
    name: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    issuer_di_ds: Union[Unset, None, str] = UNSET,
    credential_types: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Optional[Union[BadRequest, InternalServerError, VerificationPolicyPage]]:
    """Lookup verification policies by query

     Lookup verification policies by `name`, `attributes`, `issuerDIDs`, and `credentialTypes` and
    control the pagination by `offset` and `limit` parameters

    Args:
        name (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        issuer_di_ds (Union[Unset, None, str]):
        credential_types (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicyPage]]
    """

    return sync_detailed(
        client=client,
        name=name,
        attributes=attributes,
        issuer_di_ds=issuer_di_ds,
        credential_types=credential_types,
        offset=offset,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    issuer_di_ds: Union[Unset, None, str] = UNSET,
    credential_types: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Response[Union[BadRequest, InternalServerError, VerificationPolicyPage]]:
    """Lookup verification policies by query

     Lookup verification policies by `name`, `attributes`, `issuerDIDs`, and `credentialTypes` and
    control the pagination by `offset` and `limit` parameters

    Args:
        name (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        issuer_di_ds (Union[Unset, None, str]):
        credential_types (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicyPage]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        attributes=attributes,
        issuer_di_ds=issuer_di_ds,
        credential_types=credential_types,
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
    name: Union[Unset, None, str] = UNSET,
    attributes: Union[Unset, None, str] = UNSET,
    issuer_di_ds: Union[Unset, None, str] = UNSET,
    credential_types: Union[Unset, None, str] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    order: Union[Unset, None, str] = UNSET,
) -> Optional[Union[BadRequest, InternalServerError, VerificationPolicyPage]]:
    """Lookup verification policies by query

     Lookup verification policies by `name`, `attributes`, `issuerDIDs`, and `credentialTypes` and
    control the pagination by `offset` and `limit` parameters

    Args:
        name (Union[Unset, None, str]):
        attributes (Union[Unset, None, str]):
        issuer_di_ds (Union[Unset, None, str]):
        credential_types (Union[Unset, None, str]):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
        order (Union[Unset, None, str]):

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicyPage]]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            attributes=attributes,
            issuer_di_ds=issuer_di_ds,
            credential_types=credential_types,
            offset=offset,
            limit=limit,
            order=order,
        )
    ).parsed
