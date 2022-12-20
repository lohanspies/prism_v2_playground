from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.create_issue_credential_record_request import CreateIssueCredentialRecordRequest
from ...models.error_response import ErrorResponse
from ...models.issue_credential_record import IssueCredentialRecord
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateIssueCredentialRecordRequest,
) -> Dict[str, Any]:
    url = "{}/issue-credentials/credential-offers".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, IssueCredentialRecord]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = IssueCredentialRecord.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, IssueCredentialRecord]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateIssueCredentialRecordRequest,
) -> Response[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC issuer, create a new credential offer to be sent to a VC holder

    Args:
        json_body (CreateIssueCredentialRecordRequest): A request to create a new "issue
            credential record" Example: {'validityPeriod': 3600, 'awaitConfirmation': True,
            'schemaId': 'schemaId', 'claims': {'key': 'claims'}, 'automaticIssuance': True,
            'subjectId': 'did:prism:subjectofverifiablecredentials'}.

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
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
    json_body: CreateIssueCredentialRecordRequest,
) -> Optional[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC issuer, create a new credential offer to be sent to a VC holder

    Args:
        json_body (CreateIssueCredentialRecordRequest): A request to create a new "issue
            credential record" Example: {'validityPeriod': 3600, 'awaitConfirmation': True,
            'schemaId': 'schemaId', 'claims': {'key': 'claims'}, 'automaticIssuance': True,
            'subjectId': 'did:prism:subjectofverifiablecredentials'}.

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateIssueCredentialRecordRequest,
) -> Response[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC issuer, create a new credential offer to be sent to a VC holder

    Args:
        json_body (CreateIssueCredentialRecordRequest): A request to create a new "issue
            credential record" Example: {'validityPeriod': 3600, 'awaitConfirmation': True,
            'schemaId': 'schemaId', 'claims': {'key': 'claims'}, 'automaticIssuance': True,
            'subjectId': 'did:prism:subjectofverifiablecredentials'}.

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
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
    json_body: CreateIssueCredentialRecordRequest,
) -> Optional[Union[ErrorResponse, IssueCredentialRecord]]:
    """As a VC issuer, create a new credential offer to be sent to a VC holder

    Args:
        json_body (CreateIssueCredentialRecordRequest): A request to create a new "issue
            credential record" Example: {'validityPeriod': 3600, 'awaitConfirmation': True,
            'schemaId': 'schemaId', 'claims': {'key': 'claims'}, 'automaticIssuance': True,
            'subjectId': 'did:prism:subjectofverifiablecredentials'}.

    Returns:
        Response[Union[ErrorResponse, IssueCredentialRecord]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
