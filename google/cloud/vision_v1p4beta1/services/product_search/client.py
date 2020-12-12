# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from collections import OrderedDict
from distutils import util
import os
import re
from typing import Callable, Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core import client_options as client_options_lib  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.vision_v1p4beta1.services.product_search import pagers
from google.cloud.vision_v1p4beta1.types import geometry
from google.cloud.vision_v1p4beta1.types import product_search_service
from google.protobuf import empty_pb2 as empty  # type: ignore
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore

from .transports.base import ProductSearchTransport, DEFAULT_CLIENT_INFO
from .transports.grpc import ProductSearchGrpcTransport
from .transports.grpc_asyncio import ProductSearchGrpcAsyncIOTransport


class ProductSearchClientMeta(type):
    """Metaclass for the ProductSearch client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[ProductSearchTransport]]
    _transport_registry["grpc"] = ProductSearchGrpcTransport
    _transport_registry["grpc_asyncio"] = ProductSearchGrpcAsyncIOTransport

    def get_transport_class(cls, label: str = None,) -> Type[ProductSearchTransport]:
        """Return an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class ProductSearchClient(metaclass=ProductSearchClientMeta):
    """Manages Products and ProductSets of reference images for use in
    product search. It uses the following resource model:

    -  The API has a collection of
       [ProductSet][google.cloud.vision.v1p4beta1.ProductSet] resources,
       named ``projects/*/locations/*/productSets/*``, which acts as a
       way to put different products into groups to limit
       identification.

    In parallel,

    -  The API has a collection of
       [Product][google.cloud.vision.v1p4beta1.Product] resources, named
       ``projects/*/locations/*/products/*``

    -  Each [Product][google.cloud.vision.v1p4beta1.Product] has a
       collection of
       [ReferenceImage][google.cloud.vision.v1p4beta1.ReferenceImage]
       resources, named
       ``projects/*/locations/*/products/*/referenceImages/*``
    """

    @staticmethod
    def _get_default_mtls_endpoint(api_endpoint):
        """Convert api endpoint to mTLS endpoint.
        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.
        Returns:
            str: converted mTLS api endpoint.
        """
        if not api_endpoint:
            return api_endpoint

        mtls_endpoint_re = re.compile(
            r"(?P<name>[^.]+)(?P<mtls>\.mtls)?(?P<sandbox>\.sandbox)?(?P<googledomain>\.googleapis\.com)?"
        )

        m = mtls_endpoint_re.match(api_endpoint)
        name, mtls, sandbox, googledomain = m.groups()
        if mtls or not googledomain:
            return api_endpoint

        if sandbox:
            return api_endpoint.replace(
                "sandbox.googleapis.com", "mtls.sandbox.googleapis.com"
            )

        return api_endpoint.replace(".googleapis.com", ".mtls.googleapis.com")

    DEFAULT_ENDPOINT = "vision.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(  # type: ignore
        DEFAULT_ENDPOINT
    )

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            {@api.name}: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ProductSearchTransport:
        """Return the transport used by the client instance.

        Returns:
            ProductSearchTransport: The transport used by the client instance.
        """
        return self._transport

    @staticmethod
    def product_path(project: str, location: str, product: str,) -> str:
        """Return a fully-qualified product string."""
        return "projects/{project}/locations/{location}/products/{product}".format(
            project=project, location=location, product=product,
        )

    @staticmethod
    def parse_product_path(path: str) -> Dict[str, str]:
        """Parse a product path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/products/(?P<product>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def product_set_path(project: str, location: str, product_set: str,) -> str:
        """Return a fully-qualified product_set string."""
        return "projects/{project}/locations/{location}/productSets/{product_set}".format(
            project=project, location=location, product_set=product_set,
        )

    @staticmethod
    def parse_product_set_path(path: str) -> Dict[str, str]:
        """Parse a product_set path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/productSets/(?P<product_set>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def reference_image_path(
        project: str, location: str, product: str, reference_image: str,
    ) -> str:
        """Return a fully-qualified reference_image string."""
        return "projects/{project}/locations/{location}/products/{product}/referenceImages/{reference_image}".format(
            project=project,
            location=location,
            product=product,
            reference_image=reference_image,
        )

    @staticmethod
    def parse_reference_image_path(path: str) -> Dict[str, str]:
        """Parse a reference_image path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/products/(?P<product>.+?)/referenceImages/(?P<reference_image>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(billing_account: str,) -> str:
        """Return a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(folder: str,) -> str:
        """Return a fully-qualified folder string."""
        return "folders/{folder}".format(folder=folder,)

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(organization: str,) -> str:
        """Return a fully-qualified organization string."""
        return "organizations/{organization}".format(organization=organization,)

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(project: str,) -> str:
        """Return a fully-qualified project string."""
        return "projects/{project}".format(project=project,)

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(project: str, location: str,) -> str:
        """Return a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project, location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    def __init__(
        self,
        *,
        credentials: Optional[credentials.Credentials] = None,
        transport: Union[str, ProductSearchTransport, None] = None,
        client_options: Optional[client_options_lib.ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the product search client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ProductSearchTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (client_options_lib.ClientOptions): Custom options for the
                client. It won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
        if client_options is None:
            client_options = client_options_lib.ClientOptions()

        # Create SSL credentials for mutual TLS if needed.
        use_client_cert = bool(
            util.strtobool(os.getenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"))
        )

        ssl_credentials = None
        is_mtls = False
        if use_client_cert:
            if client_options.client_cert_source:
                import grpc  # type: ignore

                cert, key = client_options.client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
                is_mtls = True
            else:
                creds = SslCredentials()
                is_mtls = creds.is_mtls
                ssl_credentials = creds.ssl_credentials if is_mtls else None

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        else:
            use_mtls_env = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
            if use_mtls_env == "never":
                api_endpoint = self.DEFAULT_ENDPOINT
            elif use_mtls_env == "always":
                api_endpoint = self.DEFAULT_MTLS_ENDPOINT
            elif use_mtls_env == "auto":
                api_endpoint = (
                    self.DEFAULT_MTLS_ENDPOINT if is_mtls else self.DEFAULT_ENDPOINT
                )
            else:
                raise MutualTLSChannelError(
                    "Unsupported GOOGLE_API_USE_MTLS_ENDPOINT value. Accepted values: never, auto, always"
                )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        if isinstance(transport, ProductSearchTransport):
            # transport is a ProductSearchTransport instance.
            if credentials or client_options.credentials_file:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its scopes directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)
            self._transport = Transport(
                credentials=credentials,
                credentials_file=client_options.credentials_file,
                host=api_endpoint,
                scopes=client_options.scopes,
                ssl_channel_credentials=ssl_credentials,
                quota_project_id=client_options.quota_project_id,
                client_info=client_info,
            )

    def create_product_set(
        self,
        request: product_search_service.CreateProductSetRequest = None,
        *,
        parent: str = None,
        product_set: product_search_service.ProductSet = None,
        product_set_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.ProductSet:
        r"""Creates and returns a new ProductSet resource.

        Possible errors:

        -  Returns INVALID_ARGUMENT if display_name is missing, or is
           longer than 4096 characters.

        Args:
            request (:class:`~.product_search_service.CreateProductSetRequest`):
                The request object. Request message for the
                `CreateProductSet` method.
            parent (:class:`str`):
                Required. The project in which the ProductSet should be
                created.

                Format is ``projects/PROJECT_ID/locations/LOC_ID``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product_set (:class:`~.product_search_service.ProductSet`):
                Required. The ProductSet to create.
                This corresponds to the ``product_set`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product_set_id (:class:`str`):
                A user-supplied resource id for this ProductSet. If set,
                the server will attempt to use this value as the
                resource id. If it is already in use, an error is
                returned with code ALREADY_EXISTS. Must be at most 128
                characters long. It cannot contain the character ``/``.
                This corresponds to the ``product_set_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.ProductSet:
                A ProductSet contains Products. A
                ProductSet can contain a maximum of 1
                million reference images. If the limit
                is exceeded, periodic indexing will
                fail.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, product_set, product_set_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.CreateProductSetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.CreateProductSetRequest):
            request = product_search_service.CreateProductSetRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent
            if product_set is not None:
                request.product_set = product_set
            if product_set_id is not None:
                request.product_set_id = product_set_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_product_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_product_sets(
        self,
        request: product_search_service.ListProductSetsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProductSetsPager:
        r"""Lists ProductSets in an unspecified order.

        Possible errors:

        -  Returns INVALID_ARGUMENT if page_size is greater than 100, or
           less than 1.

        Args:
            request (:class:`~.product_search_service.ListProductSetsRequest`):
                The request object. Request message for the
                `ListProductSets` method.
            parent (:class:`str`):
                Required. The project from which ProductSets should be
                listed.

                Format is ``projects/PROJECT_ID/locations/LOC_ID``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListProductSetsPager:
                Response message for the ``ListProductSets`` method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.ListProductSetsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.ListProductSetsRequest):
            request = product_search_service.ListProductSetsRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_product_sets]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListProductSetsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_product_set(
        self,
        request: product_search_service.GetProductSetRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.ProductSet:
        r"""Gets information associated with a ProductSet.

        Possible errors:

        -  Returns NOT_FOUND if the ProductSet does not exist.

        Args:
            request (:class:`~.product_search_service.GetProductSetRequest`):
                The request object. Request message for the
                `GetProductSet` method.
            name (:class:`str`):
                Required. Resource name of the ProductSet to get.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.ProductSet:
                A ProductSet contains Products. A
                ProductSet can contain a maximum of 1
                million reference images. If the limit
                is exceeded, periodic indexing will
                fail.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.GetProductSetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.GetProductSetRequest):
            request = product_search_service.GetProductSetRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_product_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_product_set(
        self,
        request: product_search_service.UpdateProductSetRequest = None,
        *,
        product_set: product_search_service.ProductSet = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.ProductSet:
        r"""Makes changes to a ProductSet resource. Only display_name can be
        updated currently.

        Possible errors:

        -  Returns NOT_FOUND if the ProductSet does not exist.
        -  Returns INVALID_ARGUMENT if display_name is present in
           update_mask but missing from the request or longer than 4096
           characters.

        Args:
            request (:class:`~.product_search_service.UpdateProductSetRequest`):
                The request object. Request message for the
                `UpdateProductSet` method.
            product_set (:class:`~.product_search_service.ProductSet`):
                Required. The ProductSet resource
                which replaces the one on the server.
                This corresponds to the ``product_set`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`~.field_mask.FieldMask`):
                The [FieldMask][google.protobuf.FieldMask] that
                specifies which fields to update. If update_mask isn't
                specified, all mutable fields are to be updated. Valid
                mask path is ``display_name``.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.ProductSet:
                A ProductSet contains Products. A
                ProductSet can contain a maximum of 1
                million reference images. If the limit
                is exceeded, periodic indexing will
                fail.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([product_set, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.UpdateProductSetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.UpdateProductSetRequest):
            request = product_search_service.UpdateProductSetRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if product_set is not None:
                request.product_set = product_set
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_product_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("product_set.name", request.product_set.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def delete_product_set(
        self,
        request: product_search_service.DeleteProductSetRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Permanently deletes a ProductSet. Products and
        ReferenceImages in the ProductSet are not deleted.
        The actual image files are not deleted from Google Cloud
        Storage.

        Args:
            request (:class:`~.product_search_service.DeleteProductSetRequest`):
                The request object. Request message for the
                `DeleteProductSet` method.
            name (:class:`str`):
                Required. Resource name of the ProductSet to delete.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.DeleteProductSetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.DeleteProductSetRequest):
            request = product_search_service.DeleteProductSetRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_product_set]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def create_product(
        self,
        request: product_search_service.CreateProductRequest = None,
        *,
        parent: str = None,
        product: product_search_service.Product = None,
        product_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.Product:
        r"""Creates and returns a new product resource.

        Possible errors:

        -  Returns INVALID_ARGUMENT if display_name is missing or longer
           than 4096 characters.
        -  Returns INVALID_ARGUMENT if description is longer than 4096
           characters.
        -  Returns INVALID_ARGUMENT if product_category is missing or
           invalid.

        Args:
            request (:class:`~.product_search_service.CreateProductRequest`):
                The request object. Request message for the
                `CreateProduct` method.
            parent (:class:`str`):
                Required. The project in which the Product should be
                created.

                Format is ``projects/PROJECT_ID/locations/LOC_ID``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product (:class:`~.product_search_service.Product`):
                Required. The product to create.
                This corresponds to the ``product`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product_id (:class:`str`):
                A user-supplied resource id for this Product. If set,
                the server will attempt to use this value as the
                resource id. If it is already in use, an error is
                returned with code ALREADY_EXISTS. Must be at most 128
                characters long. It cannot contain the character ``/``.
                This corresponds to the ``product_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.Product:
                A Product contains ReferenceImages.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, product, product_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.CreateProductRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.CreateProductRequest):
            request = product_search_service.CreateProductRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent
            if product is not None:
                request.product = product
            if product_id is not None:
                request.product_id = product_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_product]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def list_products(
        self,
        request: product_search_service.ListProductsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProductsPager:
        r"""Lists products in an unspecified order.

        Possible errors:

        -  Returns INVALID_ARGUMENT if page_size is greater than 100 or
           less than 1.

        Args:
            request (:class:`~.product_search_service.ListProductsRequest`):
                The request object. Request message for the
                `ListProducts` method.
            parent (:class:`str`):
                Required. The project OR ProductSet from which Products
                should be listed.

                Format: ``projects/PROJECT_ID/locations/LOC_ID``
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListProductsPager:
                Response message for the ``ListProducts`` method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.ListProductsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.ListProductsRequest):
            request = product_search_service.ListProductsRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_products]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListProductsPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_product(
        self,
        request: product_search_service.GetProductRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.Product:
        r"""Gets information associated with a Product.

        Possible errors:

        -  Returns NOT_FOUND if the Product does not exist.

        Args:
            request (:class:`~.product_search_service.GetProductRequest`):
                The request object. Request message for the `GetProduct`
                method.
            name (:class:`str`):
                Required. Resource name of the Product to get.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.Product:
                A Product contains ReferenceImages.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.GetProductRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.GetProductRequest):
            request = product_search_service.GetProductRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_product]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def update_product(
        self,
        request: product_search_service.UpdateProductRequest = None,
        *,
        product: product_search_service.Product = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.Product:
        r"""Makes changes to a Product resource. Only the ``display_name``,
        ``description``, and ``labels`` fields can be updated right now.

        If labels are updated, the change will not be reflected in
        queries until the next index time.

        Possible errors:

        -  Returns NOT_FOUND if the Product does not exist.
        -  Returns INVALID_ARGUMENT if display_name is present in
           update_mask but is missing from the request or longer than
           4096 characters.
        -  Returns INVALID_ARGUMENT if description is present in
           update_mask but is longer than 4096 characters.
        -  Returns INVALID_ARGUMENT if product_category is present in
           update_mask.

        Args:
            request (:class:`~.product_search_service.UpdateProductRequest`):
                The request object. Request message for the
                `UpdateProduct` method.
            product (:class:`~.product_search_service.Product`):
                Required. The Product resource which
                replaces the one on the server.
                product.name is immutable.
                This corresponds to the ``product`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`~.field_mask.FieldMask`):
                The [FieldMask][google.protobuf.FieldMask] that
                specifies which fields to update. If update_mask isn't
                specified, all mutable fields are to be updated. Valid
                mask paths include ``product_labels``, ``display_name``,
                and ``description``.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.Product:
                A Product contains ReferenceImages.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([product, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.UpdateProductRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.UpdateProductRequest):
            request = product_search_service.UpdateProductRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if product is not None:
                request.product = product
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_product]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("product.name", request.product.name),)
            ),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def delete_product(
        self,
        request: product_search_service.DeleteProductRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Permanently deletes a product and its reference
        images.
        Metadata of the product and all its images will be
        deleted right away, but search queries against
        ProductSets containing the product may still work until
        all related caches are refreshed.

        Args:
            request (:class:`~.product_search_service.DeleteProductRequest`):
                The request object. Request message for the
                `DeleteProduct` method.
            name (:class:`str`):
                Required. Resource name of product to delete.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.DeleteProductRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.DeleteProductRequest):
            request = product_search_service.DeleteProductRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_product]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def create_reference_image(
        self,
        request: product_search_service.CreateReferenceImageRequest = None,
        *,
        parent: str = None,
        reference_image: product_search_service.ReferenceImage = None,
        reference_image_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.ReferenceImage:
        r"""Creates and returns a new ReferenceImage resource.

        The ``bounding_poly`` field is optional. If ``bounding_poly`` is
        not specified, the system will try to detect regions of interest
        in the image that are compatible with the product_category on
        the parent product. If it is specified, detection is ALWAYS
        skipped. The system converts polygons into non-rotated
        rectangles.

        Note that the pipeline will resize the image if the image
        resolution is too large to process (above 50MP).

        Possible errors:

        -  Returns INVALID_ARGUMENT if the image_uri is missing or
           longer than 4096 characters.
        -  Returns INVALID_ARGUMENT if the product does not exist.
        -  Returns INVALID_ARGUMENT if bounding_poly is not provided,
           and nothing compatible with the parent product's
           product_category is detected.
        -  Returns INVALID_ARGUMENT if bounding_poly contains more than
           10 polygons.

        Args:
            request (:class:`~.product_search_service.CreateReferenceImageRequest`):
                The request object. Request message for the
                `CreateReferenceImage` method.
            parent (:class:`str`):
                Required. Resource name of the product in which to
                create the reference image.

                Format is
                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            reference_image (:class:`~.product_search_service.ReferenceImage`):
                Required. The reference image to
                create. If an image ID is specified, it
                is ignored.
                This corresponds to the ``reference_image`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            reference_image_id (:class:`str`):
                A user-supplied resource id for the ReferenceImage to be
                added. If set, the server will attempt to use this value
                as the resource id. If it is already in use, an error is
                returned with code ALREADY_EXISTS. Must be at most 128
                characters long. It cannot contain the character ``/``.
                This corresponds to the ``reference_image_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.ReferenceImage:
                A ``ReferenceImage`` represents a product image and its
                associated metadata, such as bounding boxes.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, reference_image, reference_image_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.CreateReferenceImageRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.CreateReferenceImageRequest):
            request = product_search_service.CreateReferenceImageRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent
            if reference_image is not None:
                request.reference_image = reference_image
            if reference_image_id is not None:
                request.reference_image_id = reference_image_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_reference_image]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def delete_reference_image(
        self,
        request: product_search_service.DeleteReferenceImageRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Permanently deletes a reference image.
        The image metadata will be deleted right away, but
        search queries against ProductSets containing the image
        may still work until all related caches are refreshed.

        The actual image files are not deleted from Google Cloud
        Storage.

        Args:
            request (:class:`~.product_search_service.DeleteReferenceImageRequest`):
                The request object. Request message for the
                `DeleteReferenceImage` method.
            name (:class:`str`):
                Required. The resource name of the reference image to
                delete.

                Format is:

                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.DeleteReferenceImageRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.DeleteReferenceImageRequest):
            request = product_search_service.DeleteReferenceImageRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_reference_image]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def list_reference_images(
        self,
        request: product_search_service.ListReferenceImagesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListReferenceImagesPager:
        r"""Lists reference images.

        Possible errors:

        -  Returns NOT_FOUND if the parent product does not exist.
        -  Returns INVALID_ARGUMENT if the page_size is greater than
           100, or less than 1.

        Args:
            request (:class:`~.product_search_service.ListReferenceImagesRequest`):
                The request object. Request message for the
                `ListReferenceImages` method.
            parent (:class:`str`):
                Required. Resource name of the product containing the
                reference images.

                Format is
                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListReferenceImagesPager:
                Response message for the ``ListReferenceImages`` method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.ListReferenceImagesRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.ListReferenceImagesRequest):
            request = product_search_service.ListReferenceImagesRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_reference_images]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListReferenceImagesPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_reference_image(
        self,
        request: product_search_service.GetReferenceImageRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> product_search_service.ReferenceImage:
        r"""Gets information associated with a ReferenceImage.

        Possible errors:

        -  Returns NOT_FOUND if the specified image does not exist.

        Args:
            request (:class:`~.product_search_service.GetReferenceImageRequest`):
                The request object. Request message for the
                `GetReferenceImage` method.
            name (:class:`str`):
                Required. The resource name of the ReferenceImage to
                get.

                Format is:

                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID/referenceImages/IMAGE_ID``.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.product_search_service.ReferenceImage:
                A ``ReferenceImage`` represents a product image and its
                associated metadata, such as bounding boxes.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.GetReferenceImageRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.GetReferenceImageRequest):
            request = product_search_service.GetReferenceImageRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_reference_image]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    def add_product_to_product_set(
        self,
        request: product_search_service.AddProductToProductSetRequest = None,
        *,
        name: str = None,
        product: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Adds a Product to the specified ProductSet. If the Product is
        already present, no change is made.

        One Product can be added to at most 100 ProductSets.

        Possible errors:

        -  Returns NOT_FOUND if the Product or the ProductSet doesn't
           exist.

        Args:
            request (:class:`~.product_search_service.AddProductToProductSetRequest`):
                The request object. Request message for the
                `AddProductToProductSet` method.
            name (:class:`str`):
                Required. The resource name for the ProductSet to
                modify.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product (:class:`str`):
                Required. The resource name for the Product to be added
                to this ProductSet.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``
                This corresponds to the ``product`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, product])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.AddProductToProductSetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, product_search_service.AddProductToProductSetRequest
        ):
            request = product_search_service.AddProductToProductSetRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name
            if product is not None:
                request.product = product

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.add_product_to_product_set
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def remove_product_from_product_set(
        self,
        request: product_search_service.RemoveProductFromProductSetRequest = None,
        *,
        name: str = None,
        product: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Removes a Product from the specified ProductSet.

        Args:
            request (:class:`~.product_search_service.RemoveProductFromProductSetRequest`):
                The request object. Request message for the
                `RemoveProductFromProductSet` method.
            name (:class:`str`):
                Required. The resource name for the ProductSet to
                modify.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            product (:class:`str`):
                Required. The resource name for the Product to be
                removed from this ProductSet.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``
                This corresponds to the ``product`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, product])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.RemoveProductFromProductSetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, product_search_service.RemoveProductFromProductSetRequest
        ):
            request = product_search_service.RemoveProductFromProductSetRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name
            if product is not None:
                request.product = product

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.remove_product_from_product_set
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    def list_products_in_product_set(
        self,
        request: product_search_service.ListProductsInProductSetRequest = None,
        *,
        name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListProductsInProductSetPager:
        r"""Lists the Products in a ProductSet, in an unspecified order. If
        the ProductSet does not exist, the products field of the
        response will be empty.

        Possible errors:

        -  Returns INVALID_ARGUMENT if page_size is greater than 100 or
           less than 1.

        Args:
            request (:class:`~.product_search_service.ListProductsInProductSetRequest`):
                The request object. Request message for the
                `ListProductsInProductSet` method.
            name (:class:`str`):
                Required. The ProductSet resource for which to retrieve
                Products.

                Format is:
                ``projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID``
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListProductsInProductSetPager:
                Response message for the ``ListProductsInProductSet``
                method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.ListProductsInProductSetRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(
            request, product_search_service.ListProductsInProductSetRequest
        ):
            request = product_search_service.ListProductsInProductSetRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_products_in_product_set
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListProductsInProductSetPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    def import_product_sets(
        self,
        request: product_search_service.ImportProductSetsRequest = None,
        *,
        parent: str = None,
        input_config: product_search_service.ImportProductSetsInputConfig = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Asynchronous API that imports a list of reference images to
        specified product sets based on a list of image information.

        The [google.longrunning.Operation][google.longrunning.Operation]
        API can be used to keep track of the progress and results of the
        request. ``Operation.metadata`` contains
        ``BatchOperationMetadata``. (progress) ``Operation.response``
        contains ``ImportProductSetsResponse``. (results)

        The input source of this method is a csv file on Google Cloud
        Storage. For the format of the csv file please see
        [ImportProductSetsGcsSource.csv_file_uri][google.cloud.vision.v1p4beta1.ImportProductSetsGcsSource.csv_file_uri].

        Args:
            request (:class:`~.product_search_service.ImportProductSetsRequest`):
                The request object. Request message for the
                `ImportProductSets` method.
            parent (:class:`str`):
                Required. The project in which the ProductSets should be
                imported.

                Format is ``projects/PROJECT_ID/locations/LOC_ID``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            input_config (:class:`~.product_search_service.ImportProductSetsInputConfig`):
                Required. The input content for the
                list of requests.
                This corresponds to the ``input_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.product_search_service.ImportProductSetsResponse``:
                Response message for the ``ImportProductSets`` method.

                This message is returned by the
                [google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]
                method in the returned
                [google.longrunning.Operation.response][google.longrunning.Operation.response]
                field.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, input_config])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.ImportProductSetsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.ImportProductSetsRequest):
            request = product_search_service.ImportProductSetsRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent
            if input_config is not None:
                request.input_config = input_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.import_product_sets]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            product_search_service.ImportProductSetsResponse,
            metadata_type=product_search_service.BatchOperationMetadata,
        )

        # Done; return the response.
        return response

    def purge_products(
        self,
        request: product_search_service.PurgeProductsRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation.Operation:
        r"""Asynchronous API to delete all Products in a ProductSet or all
        Products that are in no ProductSet.

        If a Product is a member of the specified ProductSet in addition
        to other ProductSets, the Product will still be deleted.

        It is recommended to not delete the specified ProductSet until
        after this operation has completed. It is also recommended to
        not add any of the Products involved in the batch delete to a
        new ProductSet while this operation is running because those
        Products may still end up deleted.

        It's not possible to undo the PurgeProducts operation.
        Therefore, it is recommended to keep the csv files used in
        ImportProductSets (if that was how you originally built the
        Product Set) before starting PurgeProducts, in case you need to
        re-import the data after deletion.

        If the plan is to purge all of the Products from a ProductSet
        and then re-use the empty ProductSet to re-import new Products
        into the empty ProductSet, you must wait until the PurgeProducts
        operation has finished for that ProductSet.

        The [google.longrunning.Operation][google.longrunning.Operation]
        API can be used to keep track of the progress and results of the
        request. ``Operation.metadata`` contains
        ``BatchOperationMetadata``. (progress)

        Args:
            request (:class:`~.product_search_service.PurgeProductsRequest`):
                The request object. Request message for the
                `PurgeProducts` method.
            parent (:class:`str`):
                Required. The project and location in which the Products
                should be deleted.

                Format is ``projects/PROJECT_ID/locations/LOC_ID``.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.empty.Empty``: A generic empty message that
                you can re-use to avoid defining duplicated empty
                messages in your APIs. A typical example is to use it as
                the request or the response type of an API method. For
                instance:

                ::

                    service Foo {
                      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
                    }

                The JSON representation for ``Empty`` is empty JSON
                object ``{}``.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # Minor optimization to avoid making a copy if the user passes
        # in a product_search_service.PurgeProductsRequest.
        # There's no risk of modifying the input as we've already verified
        # there are no flattened fields.
        if not isinstance(request, product_search_service.PurgeProductsRequest):
            request = product_search_service.PurgeProductsRequest(request)

            # If we have keyword arguments corresponding to fields on the
            # request, apply these.

            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.purge_products]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty.Empty,
            metadata_type=product_search_service.BatchOperationMetadata,
        )

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-vision",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ProductSearchClient",)
