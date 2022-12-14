from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bad_request import BadRequest
from ...models.internal_server_error import InternalServerError
from ...models.verification_policy import VerificationPolicy
from ...models.verification_policy_input import VerificationPolicyInput
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: VerificationPolicyInput,
) -> Dict[str, Any]:
    url = "{}/verification/policies".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[BadRequest, InternalServerError, VerificationPolicy]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = VerificationPolicy.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[BadRequest, InternalServerError, VerificationPolicy]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: VerificationPolicyInput,
) -> Response[Union[BadRequest, InternalServerError, VerificationPolicy]]:
    """Create the new verification policy

     Create the new verification policy

    Args:
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicy]]
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
    json_body: VerificationPolicyInput,
) -> Optional[Union[BadRequest, InternalServerError, VerificationPolicy]]:
    """Create the new verification policy

     Create the new verification policy

    Args:
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicy]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: VerificationPolicyInput,
) -> Response[Union[BadRequest, InternalServerError, VerificationPolicy]]:
    """Create the new verification policy

     Create the new verification policy

    Args:
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicy]]
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
    json_body: VerificationPolicyInput,
) -> Optional[Union[BadRequest, InternalServerError, VerificationPolicy]]:
    """Create the new verification policy

     Create the new verification policy

    Args:
        json_body (VerificationPolicyInput):  Example: {'issuerDIDs': ['issuerDIDs',
            'issuerDIDs'], 'createdAt': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'name': 'name', 'credentialTypes': ['credentialTypes',
            'credentialTypes'], 'attributes': ['attributes', 'attributes'], 'id': 'id', 'updatedAt':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[Union[BadRequest, InternalServerError, VerificationPolicy]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
