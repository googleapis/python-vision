# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.vision.v1p2beta1 ImageAnnotator API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.grpc_helpers
import google.api_core.operation
from google.api_core import operations_v1
import grpc

from google.cloud.vision_v1p2beta1.gapic import enums
from google.cloud.vision_v1p2beta1.gapic import image_annotator_client_config
from google.cloud.vision_v1p2beta1.gapic.transports import (
    image_annotator_grpc_transport,
)
from google.cloud.vision_v1p2beta1.proto import image_annotator_pb2
from google.cloud.vision_v1p2beta1.proto import image_annotator_pb2_grpc
from google.longrunning import operations_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-vision").version


class ImageAnnotatorClient(object):
    """
    Service that performs Google Cloud Vision API detection tasks over client
    images, such as face, landmark, logo, label, and text detection. The
    ImageAnnotator service returns detected entities from the images.
    """

    SERVICE_ADDRESS = "vision.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.vision.v1p2beta1.ImageAnnotator"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ImageAnnotatorClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.ImageAnnotatorGrpcTransport,
                    Callable[[~.Credentials, type], ~.ImageAnnotatorGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = image_annotator_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=image_annotator_grpc_transport.ImageAnnotatorGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = image_annotator_grpc_transport.ImageAnnotatorGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def batch_annotate_images(
        self,
        requests,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Run image detection and annotation for a batch of images.

        Example:
            >>> from google.cloud import vision_v1p2beta1
            >>>
            >>> client = vision_v1p2beta1.ImageAnnotatorClient()
            >>>
            >>> # TODO: Initialize `requests`:
            >>> requests = []
            >>>
            >>> response = client.batch_annotate_images(requests)

        Args:
            requests (list[Union[dict, ~google.cloud.vision_v1p2beta1.types.AnnotateImageRequest]]): Required. Individual image annotation requests for this batch.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.vision_v1p2beta1.types.AnnotateImageRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.vision_v1p2beta1.types.BatchAnnotateImagesResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_annotate_images" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_annotate_images"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_annotate_images,
                default_retry=self._method_configs["BatchAnnotateImages"].retry,
                default_timeout=self._method_configs["BatchAnnotateImages"].timeout,
                client_info=self._client_info,
            )

        request = image_annotator_pb2.BatchAnnotateImagesRequest(requests=requests)
        return self._inner_api_calls["batch_annotate_images"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def async_batch_annotate_files(
        self,
        requests,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Run async image detection and annotation for a list of generic files
        (e.g. PDF) which may contain multiple pages and multiple images per
        page. Progress and results can be retrieved through the
        ``google.longrunning.Operations`` interface. ``Operation.metadata``
        contains ``OperationMetadata`` (metadata). ``Operation.response``
        contains ``AsyncBatchAnnotateFilesResponse`` (results).

        Example:
            >>> from google.cloud import vision_v1p2beta1
            >>>
            >>> client = vision_v1p2beta1.ImageAnnotatorClient()
            >>>
            >>> # TODO: Initialize `requests`:
            >>> requests = []
            >>>
            >>> response = client.async_batch_annotate_files(requests)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            requests (list[Union[dict, ~google.cloud.vision_v1p2beta1.types.AsyncAnnotateFileRequest]]): Required. Individual async file annotation requests for this batch.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.vision_v1p2beta1.types.AsyncAnnotateFileRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.vision_v1p2beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "async_batch_annotate_files" not in self._inner_api_calls:
            self._inner_api_calls[
                "async_batch_annotate_files"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.async_batch_annotate_files,
                default_retry=self._method_configs["AsyncBatchAnnotateFiles"].retry,
                default_timeout=self._method_configs["AsyncBatchAnnotateFiles"].timeout,
                client_info=self._client_info,
            )

        request = image_annotator_pb2.AsyncBatchAnnotateFilesRequest(requests=requests)
        operation = self._inner_api_calls["async_batch_annotate_files"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            image_annotator_pb2.AsyncBatchAnnotateFilesResponse,
            metadata_type=image_annotator_pb2.OperationMetadata,
        )
