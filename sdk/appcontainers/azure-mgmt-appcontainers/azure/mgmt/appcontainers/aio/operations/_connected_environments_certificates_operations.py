# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._connected_environments_certificates_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)
from .._vendor import ContainerAppsAPIClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ConnectedEnvironmentsCertificatesOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.appcontainers.aio.ContainerAppsAPIClient`'s
        :attr:`connected_environments_certificates` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, resource_group_name: str, connected_environment_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.Certificate"]:
        """Get the Certificates in a given connected environment.

        Get the Certificates in a given connected environment.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :return: An iterator like instance of either Certificate or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.appcontainers.models.Certificate]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.CertificateCollection] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    resource_group_name=resource_group_name,
                    connected_environment_name=connected_environment_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("CertificateCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, connected_environment_name: str, certificate_name: str, **kwargs: Any
    ) -> _models.Certificate:
        """Get the specified Certificate.

        Get the specified Certificate.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Certificate] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Certificate", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        certificate_name: str,
        certificate_envelope: Optional[_models.Certificate] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Create or Update a Certificate.

        Create or Update a Certificate.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :param certificate_envelope: Certificate to be created or updated. Default value is None.
        :type certificate_envelope: ~azure.mgmt.appcontainers.models.Certificate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        certificate_name: str,
        certificate_envelope: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Create or Update a Certificate.

        Create or Update a Certificate.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :param certificate_envelope: Certificate to be created or updated. Default value is None.
        :type certificate_envelope: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        certificate_name: str,
        certificate_envelope: Optional[Union[_models.Certificate, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.Certificate:
        """Create or Update a Certificate.

        Create or Update a Certificate.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :param certificate_envelope: Certificate to be created or updated. Is either a Certificate type
         or a IO[bytes] type. Default value is None.
        :type certificate_envelope: ~azure.mgmt.appcontainers.models.Certificate or IO[bytes]
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Certificate] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(certificate_envelope, (IOBase, bytes)):
            _content = certificate_envelope
        else:
            if certificate_envelope is not None:
                _json = self._serialize.body(certificate_envelope, "Certificate")
            else:
                _json = None

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Certificate", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, connected_environment_name: str, certificate_name: str, **kwargs: Any
    ) -> None:
        """Deletes the specified Certificate.

        Deletes the specified Certificate.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        certificate_name: str,
        certificate_envelope: _models.CertificatePatch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Update properties of a certificate.

        Patches a certificate. Currently only patching of tags is supported.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :param certificate_envelope: Properties of a certificate that need to be updated. Required.
        :type certificate_envelope: ~azure.mgmt.appcontainers.models.CertificatePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        certificate_name: str,
        certificate_envelope: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Update properties of a certificate.

        Patches a certificate. Currently only patching of tags is supported.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :param certificate_envelope: Properties of a certificate that need to be updated. Required.
        :type certificate_envelope: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        connected_environment_name: str,
        certificate_name: str,
        certificate_envelope: Union[_models.CertificatePatch, IO[bytes]],
        **kwargs: Any
    ) -> _models.Certificate:
        """Update properties of a certificate.

        Patches a certificate. Currently only patching of tags is supported.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param connected_environment_name: Name of the Connected Environment. Required.
        :type connected_environment_name: str
        :param certificate_name: Name of the Certificate. Required.
        :type certificate_name: str
        :param certificate_envelope: Properties of a certificate that need to be updated. Is either a
         CertificatePatch type or a IO[bytes] type. Required.
        :type certificate_envelope: ~azure.mgmt.appcontainers.models.CertificatePatch or IO[bytes]
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Certificate] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(certificate_envelope, (IOBase, bytes)):
            _content = certificate_envelope
        else:
            _json = self._serialize.body(certificate_envelope, "CertificatePatch")

        _request = build_update_request(
            resource_group_name=resource_group_name,
            connected_environment_name=connected_environment_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Certificate", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
