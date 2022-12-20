from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.issue_credential_record_collection import IssueCredentialRecordCollection
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/issue-credentials/records".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, IssueCredentialRecordCollection]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IssueCredentialRecordCollection.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, IssueCredentialRecordCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[ErrorResponse, IssueCredentialRecordCollection]]:
    """Get credential records

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecordCollection]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, IssueCredentialRecordCollection]]:
    """Get credential records

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecordCollection]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[ErrorResponse, IssueCredentialRecordCollection]]:
    """Get credential records

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecordCollection]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, IssueCredentialRecordCollection]]:
    """Get credential records

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecordCollection]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
