from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.authentication_challenge_submission_request import AuthenticationChallengeSubmissionRequest
from ...models.authentication_challenge_submission_response import AuthenticationChallengeSubmissionResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AuthenticationChallengeSubmissionRequest,
) -> Dict[str, Any]:
    url = "{}/authentication/challenge-submissions".format(client.base_url)

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
    *, client: Client, response: httpx.Response
) -> Optional[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuthenticationChallengeSubmissionResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AuthenticationChallengeSubmissionRequest,
) -> Response[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]:
    """Create a verification from challenge

     Submit a challenge submission that will be verified by Castor for a relying-party.

    Args:
        json_body (AuthenticationChallengeSubmissionRequest):  Example: {'signature':
            '243b9ed6561ab3...5d497f609b8cd04', 'subject': 'did:example:123456789abcdefghi',
            'challenge': 'eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: AuthenticationChallengeSubmissionRequest,
) -> Optional[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]:
    """Create a verification from challenge

     Submit a challenge submission that will be verified by Castor for a relying-party.

    Args:
        json_body (AuthenticationChallengeSubmissionRequest):  Example: {'signature':
            '243b9ed6561ab3...5d497f609b8cd04', 'subject': 'did:example:123456789abcdefghi',
            'challenge': 'eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AuthenticationChallengeSubmissionRequest,
) -> Response[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]:
    """Create a verification from challenge

     Submit a challenge submission that will be verified by Castor for a relying-party.

    Args:
        json_body (AuthenticationChallengeSubmissionRequest):  Example: {'signature':
            '243b9ed6561ab3...5d497f609b8cd04', 'subject': 'did:example:123456789abcdefghi',
            'challenge': 'eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: AuthenticationChallengeSubmissionRequest,
) -> Optional[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]:
    """Create a verification from challenge

     Submit a challenge submission that will be verified by Castor for a relying-party.

    Args:
        json_body (AuthenticationChallengeSubmissionRequest):  Example: {'signature':
            '243b9ed6561ab3...5d497f609b8cd04', 'subject': 'did:example:123456789abcdefghi',
            'challenge': 'eyJhbGciOiJIUzI1NiIsInR5c...0eu8Ri_WSPSsBTlCes2YMpuB1mHU'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationChallengeSubmissionResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
