from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.create_authentication_challenge_request import CreateAuthenticationChallengeRequest
from ...models.create_authentication_challenge_response import CreateAuthenticationChallengeResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateAuthenticationChallengeRequest,
) -> Dict[str, Any]:
    url = "{}/authentication/challenges".format(client.base_url)

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
) -> Optional[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateAuthenticationChallengeResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateAuthenticationChallengeRequest,
) -> Response[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]:
    """Create a new authentication challenge

     Create a new authentication challenge that will be later verified
    by Castor for a relying-party.

    Args:
        json_body (CreateAuthenticationChallengeRequest):  Example: {'subject':
            'did:example:123456789abcdefghi', 'state': 'qrcode#123', 'ttl': 900}.

    Returns:
        Response[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]
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
    json_body: CreateAuthenticationChallengeRequest,
) -> Optional[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]:
    """Create a new authentication challenge

     Create a new authentication challenge that will be later verified
    by Castor for a relying-party.

    Args:
        json_body (CreateAuthenticationChallengeRequest):  Example: {'subject':
            'did:example:123456789abcdefghi', 'state': 'qrcode#123', 'ttl': 900}.

    Returns:
        Response[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateAuthenticationChallengeRequest,
) -> Response[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]:
    """Create a new authentication challenge

     Create a new authentication challenge that will be later verified
    by Castor for a relying-party.

    Args:
        json_body (CreateAuthenticationChallengeRequest):  Example: {'subject':
            'did:example:123456789abcdefghi', 'state': 'qrcode#123', 'ttl': 900}.

    Returns:
        Response[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]
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
    json_body: CreateAuthenticationChallengeRequest,
) -> Optional[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]:
    """Create a new authentication challenge

     Create a new authentication challenge that will be later verified
    by Castor for a relying-party.

    Args:
        json_body (CreateAuthenticationChallengeRequest):  Example: {'subject':
            'did:example:123456789abcdefghi', 'state': 'qrcode#123', 'ttl': 900}.

    Returns:
        Response[Union[CreateAuthenticationChallengeResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
