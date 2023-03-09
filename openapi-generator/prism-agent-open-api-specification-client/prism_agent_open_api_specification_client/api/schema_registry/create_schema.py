from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.internal_server_error import InternalServerError
from ...models.verifiable_credential_schema import VerifiableCredentialSchema
from ...models.verification_credential_schema_input import VerificationCredentialSchemaInput
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: VerificationCredentialSchemaInput,
) -> Dict[str, Any]:
    url = "{}/schema-registry/schemas".format(client.base_url)

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
) -> Optional[Union[InternalServerError, VerifiableCredentialSchema]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = VerifiableCredentialSchema.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[InternalServerError, VerifiableCredentialSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: VerificationCredentialSchemaInput,
) -> Response[Union[InternalServerError, VerifiableCredentialSchema]]:
    """Publish new schema to the schema registry

     Publish the new schema with attributes to the schema registry on behalf of Cloud Agent. Schema will
    be signed by the keys of Cloud Agent and issued by the DID that corresponds to it

    Args:
        json_body (VerificationCredentialSchemaInput):  Example: {'authored':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'name': 'name',
            'description': 'description', 'attributes': ['attributes', 'attributes'], 'id':
            '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'version': 'version', 'tags': ['tags', 'tags']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchema]]
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
    json_body: VerificationCredentialSchemaInput,
) -> Optional[Union[InternalServerError, VerifiableCredentialSchema]]:
    """Publish new schema to the schema registry

     Publish the new schema with attributes to the schema registry on behalf of Cloud Agent. Schema will
    be signed by the keys of Cloud Agent and issued by the DID that corresponds to it

    Args:
        json_body (VerificationCredentialSchemaInput):  Example: {'authored':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'name': 'name',
            'description': 'description', 'attributes': ['attributes', 'attributes'], 'id':
            '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'version': 'version', 'tags': ['tags', 'tags']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchema]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: VerificationCredentialSchemaInput,
) -> Response[Union[InternalServerError, VerifiableCredentialSchema]]:
    """Publish new schema to the schema registry

     Publish the new schema with attributes to the schema registry on behalf of Cloud Agent. Schema will
    be signed by the keys of Cloud Agent and issued by the DID that corresponds to it

    Args:
        json_body (VerificationCredentialSchemaInput):  Example: {'authored':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'name': 'name',
            'description': 'description', 'attributes': ['attributes', 'attributes'], 'id':
            '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'version': 'version', 'tags': ['tags', 'tags']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchema]]
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
    json_body: VerificationCredentialSchemaInput,
) -> Optional[Union[InternalServerError, VerifiableCredentialSchema]]:
    """Publish new schema to the schema registry

     Publish the new schema with attributes to the schema registry on behalf of Cloud Agent. Schema will
    be signed by the keys of Cloud Agent and issued by the DID that corresponds to it

    Args:
        json_body (VerificationCredentialSchemaInput):  Example: {'authored':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'name': 'name',
            'description': 'description', 'attributes': ['attributes', 'attributes'], 'id':
            '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'version': 'version', 'tags': ['tags', 'tags']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InternalServerError, VerifiableCredentialSchema]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
