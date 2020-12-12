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
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.vision_v1p3beta1.types import image_annotator

from .transports.base import ImageAnnotatorTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ImageAnnotatorGrpcAsyncIOTransport
from .client import ImageAnnotatorClient


class ImageAnnotatorAsyncClient:
    """Service that performs Google Cloud Vision API detection tasks
    over client images, such as face, landmark, logo, label, and
    text detection. The ImageAnnotator service returns detected
    entities from the images.
    """

    _client: ImageAnnotatorClient

    DEFAULT_ENDPOINT = ImageAnnotatorClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ImageAnnotatorClient.DEFAULT_MTLS_ENDPOINT

    product_path = staticmethod(ImageAnnotatorClient.product_path)
    parse_product_path = staticmethod(ImageAnnotatorClient.parse_product_path)
    product_set_path = staticmethod(ImageAnnotatorClient.product_set_path)
    parse_product_set_path = staticmethod(ImageAnnotatorClient.parse_product_set_path)

    common_billing_account_path = staticmethod(
        ImageAnnotatorClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ImageAnnotatorClient.parse_common_billing_account_path
    )

    common_folder_path = staticmethod(ImageAnnotatorClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ImageAnnotatorClient.parse_common_folder_path
    )

    common_organization_path = staticmethod(
        ImageAnnotatorClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ImageAnnotatorClient.parse_common_organization_path
    )

    common_project_path = staticmethod(ImageAnnotatorClient.common_project_path)
    parse_common_project_path = staticmethod(
        ImageAnnotatorClient.parse_common_project_path
    )

    common_location_path = staticmethod(ImageAnnotatorClient.common_location_path)
    parse_common_location_path = staticmethod(
        ImageAnnotatorClient.parse_common_location_path
    )

    from_service_account_file = ImageAnnotatorClient.from_service_account_file
    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ImageAnnotatorTransport:
        """Return the transport used by the client instance.

        Returns:
            ImageAnnotatorTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ImageAnnotatorClient).get_transport_class, type(ImageAnnotatorClient)
    )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, ImageAnnotatorTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the image annotator client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ImageAnnotatorTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
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

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """

        self._client = ImageAnnotatorClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def batch_annotate_images(
        self,
        request: image_annotator.BatchAnnotateImagesRequest = None,
        *,
        requests: Sequence[image_annotator.AnnotateImageRequest] = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> image_annotator.BatchAnnotateImagesResponse:
        r"""Run image detection and annotation for a batch of
        images.

        Args:
            request (:class:`~.image_annotator.BatchAnnotateImagesRequest`):
                The request object. Multiple image annotation requests
                are batched into a single service call.
            requests (:class:`Sequence[~.image_annotator.AnnotateImageRequest]`):
                Individual image annotation requests
                for this batch.
                This corresponds to the ``requests`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.image_annotator.BatchAnnotateImagesResponse:
                Response to a batch image annotation
                request.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([requests])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = image_annotator.BatchAnnotateImagesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if requests:
            request.requests.extend(requests)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_annotate_images,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    exceptions.DeadlineExceeded, exceptions.ServiceUnavailable,
                ),
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def async_batch_annotate_files(
        self,
        request: image_annotator.AsyncBatchAnnotateFilesRequest = None,
        *,
        requests: Sequence[image_annotator.AsyncAnnotateFileRequest] = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Run asynchronous image detection and annotation for a list of
        generic files, such as PDF files, which may contain multiple
        pages and multiple images per page. Progress and results can be
        retrieved through the ``google.longrunning.Operations``
        interface. ``Operation.metadata`` contains ``OperationMetadata``
        (metadata). ``Operation.response`` contains
        ``AsyncBatchAnnotateFilesResponse`` (results).

        Args:
            request (:class:`~.image_annotator.AsyncBatchAnnotateFilesRequest`):
                The request object. Multiple async file annotation
                requests are batched into a single service call.
            requests (:class:`Sequence[~.image_annotator.AsyncAnnotateFileRequest]`):
                Required. Individual async file
                annotation requests for this batch.
                This corresponds to the ``requests`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:``~.image_annotator.AsyncBatchAnnotateFilesResponse``:
                Response to an async batch file annotation request.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([requests])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = image_annotator.AsyncBatchAnnotateFilesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if requests:
            request.requests.extend(requests)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.async_batch_annotate_files,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(),
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            image_annotator.AsyncBatchAnnotateFilesResponse,
            metadata_type=image_annotator.OperationMetadata,
        )

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-vision",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ImageAnnotatorAsyncClient",)
