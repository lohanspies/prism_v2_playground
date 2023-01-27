from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.bad_request import BadRequest
from ...models.internal_server_error import InternalServerError
from ...models.not_found import NotFound
from ...models.verification_policy import VerificationPolicy
from ...models.verification_policy_input import VerificationPolicyInput
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: VerificationPolicyInput,
) -> Dict[str, Any]:
    url = "{}/verification/policies/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = VerificationPolicy.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFound.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: VerificationPolicyInput,
) -> Response[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]:
    """Update the verification policy object by id

     Update the fields of the verification policy entry: `attributes`, `issuerDIDs`, `name`,
    `credentialTypes`,

    Args:
        id (str):
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]
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

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: VerificationPolicyInput,
) -> Optional[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]:
    """Update the verification policy object by id

     Update the fields of the verification policy entry: `attributes`, `issuerDIDs`, `name`,
    `credentialTypes`,

    Args:
        id (str):
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]
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
    json_body: VerificationPolicyInput,
) -> Response[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]:
    """Update the verification policy object by id

     Update the fields of the verification policy entry: `attributes`, `issuerDIDs`, `name`,
    `credentialTypes`,

    Args:
        id (str):
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: VerificationPolicyInput,
) -> Optional[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]:
    """Update the verification policy object by id

     Update the fields of the verification policy entry: `attributes`, `issuerDIDs`, `name`,
    `credentialTypes`,

    Args:
        id (str):
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, InternalServerError, NotFound, VerificationPolicy]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
