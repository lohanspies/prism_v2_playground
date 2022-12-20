from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.issue_credential_record import IssueCredentialRecord
from ...types import Response


def _get_kwargs(
    record_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/issue-credentials/records/{recordId}/accept-offer".format(client.base_url, recordId=record_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, IssueCredentialRecord]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IssueCredentialRecord.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, IssueCredentialRecord]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    record_id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC holder, accept a credential offer received from an issuer

    Args:
        record_id (str):

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    record_id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC holder, accept a credential offer received from an issuer

    Args:
        record_id (str):

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
    """

    return sync_detailed(
        record_id=record_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    record_id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC holder, accept a credential offer received from an issuer

    Args:
        record_id (str):

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    record_id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC holder, accept a credential offer received from an issuer

    Args:
        record_id (str):

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
    """

    return (
        await asyncio_detailed(
            record_id=record_id,
            client=client,
        )
    ).parsed
