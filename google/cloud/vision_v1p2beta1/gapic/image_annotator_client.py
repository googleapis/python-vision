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
        # gRPC Transcoding

        gRPC Transcoding is a feature for mapping between a gRPC method and one
        or more HTTP REST endpoints. It allows developers to build a single API
        service that supports both gRPC APIs and REST APIs. Many systems,
        including `Google APIs <https://github.com/googleapis/googleapis>`__,
        `Cloud Endpoints <https://cloud.google.com/endpoints>`__, `gRPC
        Gateway <https://github.com/grpc-ecosystem/grpc-gateway>`__, and
        `Envoy <https://github.com/envoyproxy/envoy>`__ proxy support this
        feature and use it for large scale production services.

        ``HttpRule`` defines the schema of the gRPC/REST mapping. The mapping
        specifies how different portions of the gRPC request message are mapped
        to the URL path, URL query parameters, and HTTP request body. It also
        controls how the gRPC response message is mapped to the HTTP response
        body. ``HttpRule`` is typically specified as an ``google.api.http``
        annotation on the gRPC method.

        Each mapping specifies a URL path template and an HTTP method. The path
        template may refer to one or more fields in the gRPC request message, as
        long as each field is a non-repeated field with a primitive
        (non-message) type. The path template controls how fields of the request
        message are mapped to the URL path.

        Example:

        ::

            service Messaging {
              rpc GetMessage(GetMessageRequest) returns (Message) {
                option (google.api.http) = {
                    get: "/v1/{name=messages/*}"
                };
              }
            }
            message GetMessageRequest {
              string name = 1; // Mapped to URL path.
            }
            message Message {
              string text = 1; // The resource content.
            }

        This enables an HTTP REST to gRPC mapping as below:

        HTTP \| gRPC -----|----- ``GET /v1/messages/123456`` \|
        ``GetMessage(name: "messages/123456")``

        Any fields in the request message which are not bound by the path
        template automatically become HTTP query parameters if there is no HTTP
        request body. For example:

        ::

            service Messaging {
              rpc GetMessage(GetMessageRequest) returns (Message) {
                option (google.api.http) = {
                    get:"/v1/messages/{message_id}"
                };
              }
            }
            message GetMessageRequest {
              message SubMessage {
                string subfield = 1;
              }
              string message_id = 1; // Mapped to URL path.
              int64 revision = 2;    // Mapped to URL query parameter `revision`.
              SubMessage sub = 3;    // Mapped to URL query parameter `sub.subfield`.
            }

        This enables a HTTP JSON to RPC mapping as below:

        HTTP \| gRPC -----|-----
        ``GET /v1/messages/123456?revision=2&sub.subfield=foo`` \|
        ``GetMessage(message_id: "123456" revision: 2 sub: SubMessage(subfield: "foo"))``

        Note that fields which are mapped to URL query parameters must have a
        primitive type or a repeated primitive type or a non-repeated message
        type. In the case of a repeated type, the parameter can be repeated in
        the URL as ``...?param=A&param=B``. In the case of a message type, each
        field of the message is mapped to a separate parameter, such as
        ``...?foo.a=A&foo.b=B&foo.c=C``.

        For HTTP methods that allow a request body, the ``body`` field specifies
        the mapping. Consider a REST update method on the message resource
        collection:

        ::

            service Messaging {
              rpc UpdateMessage(UpdateMessageRequest) returns (Message) {
                option (google.api.http) = {
                  patch: "/v1/messages/{message_id}"
                  body: "message"
                };
              }
            }
            message UpdateMessageRequest {
              string message_id = 1; // mapped to the URL
              Message message = 2;   // mapped to the body
            }

        The following HTTP JSON to RPC mapping is enabled, where the
        representation of the JSON in the request body is determined by protos
        JSON encoding:

        HTTP \| gRPC -----|----- ``PATCH /v1/messages/123456 { "text": "Hi!" }``
        \| ``UpdateMessage(message_id: "123456" message { text: "Hi!" })``

        The special name ``*`` can be used in the body mapping to define that
        every field not bound by the path template should be mapped to the
        request body. This enables the following alternative definition of the
        update method:

        ::

            service Messaging {
              rpc UpdateMessage(Message) returns (Message) {
                option (google.api.http) = {
                  patch: "/v1/messages/{message_id}"
                  body: "*"
                };
              }
            }
            message Message {
              string message_id = 1;
              string text = 2;
            }

        The following HTTP JSON to RPC mapping is enabled:

        HTTP \| gRPC -----|----- ``PATCH /v1/messages/123456 { "text": "Hi!" }``
        \| ``UpdateMessage(message_id: "123456" text: "Hi!")``

        Note that when using ``*`` in the body mapping, it is not possible to
        have HTTP parameters, as all fields not bound by the path end in the
        body. This makes this option more rarely used in practice when defining
        REST APIs. The common usage of ``*`` is in custom methods which don't
        use the URL at all for transferring data.

        It is possible to define multiple HTTP methods for one RPC by using the
        ``additional_bindings`` option. Example:

        ::

            service Messaging {
              rpc GetMessage(GetMessageRequest) returns (Message) {
                option (google.api.http) = {
                  get: "/v1/messages/{message_id}"
                  additional_bindings {
                    get: "/v1/users/{user_id}/messages/{message_id}"
                  }
                };
              }
            }
            message GetMessageRequest {
              string message_id = 1;
              string user_id = 2;
            }

        This enables the following two alternative HTTP JSON to RPC mappings:

        HTTP \| gRPC -----|----- ``GET /v1/messages/123456`` \|
        ``GetMessage(message_id: "123456")``
        ``GET /v1/users/me/messages/123456`` \|
        ``GetMessage(user_id: "me" message_id: "123456")``

        ## Rules for HTTP mapping

        1. Leaf request fields (recursive expansion nested messages in the
           request message) are classified into three categories:

           -  Fields referred by the path template. They are passed via the URL
              path.
           -  Fields referred by the ``HttpRule.body``. They are passed via the
              HTTP request body.
           -  All other fields are passed via the URL query parameters, and the
              parameter name is the field path in the request message. A
              repeated field can be represented as multiple query parameters
              under the same name.

        2. If ``HttpRule.body`` is "*", there is no URL query parameter, all
           fields are passed via URL path and HTTP request body.
        3. If ``HttpRule.body`` is omitted, there is no HTTP request body, all
           fields are passed via URL path and URL query parameters.

        Path template syntax
        ~~~~~~~~~~~~~~~~~~~~

        ::

            Template = "/" Segments [ Verb ] ;
            Segments = Segment { "/" Segment } ;
            Segment  = "*" | "**" | LITERAL | Variable ;
            Variable = "{" FieldPath [ "=" Segments ] "}" ;
            FieldPath = IDENT { "." IDENT } ;
            Verb     = ":" LITERAL ;

        The syntax ``*`` matches a single URL path segment. The syntax ``**``
        matches zero or more URL path segments, which must be the last part of
        the URL path except the ``Verb``.

        The syntax ``Variable`` matches part of the URL path as specified by its
        template. A variable template must not contain other variables. If a
        variable matches a single path segment, its template may be omitted,
        e.g. ``{var}`` is equivalent to ``{var=*}``.

        The syntax ``LITERAL`` matches literal text in the URL path. If the
        ``LITERAL`` contains any reserved character, such characters should be
        percent-encoded before the matching.

        If a variable contains exactly one path segment, such as ``"{var}"`` or
        ``"{var=*}"``, when such a variable is expanded into a URL path on the
        client side, all characters except ``[-_.~0-9a-zA-Z]`` are
        percent-encoded. The server side does the reverse decoding. Such
        variables show up in the `Discovery
        Document <https://developers.google.com/discovery/v1/reference/apis>`__
        as ``{var}``.

        If a variable contains multiple path segments, such as ``"{var=foo/*}"``
        or ``"{var=**}"``, when such a variable is expanded into a URL path on
        the client side, all characters except ``[-_.~/0-9a-zA-Z]`` are
        percent-encoded. The server side does the reverse decoding, except "%2F"
        and "%2f" are left unchanged. Such variables show up in the `Discovery
        Document <https://developers.google.com/discovery/v1/reference/apis>`__
        as ``{+var}``.

        ## Using gRPC API Service Configuration

        gRPC API Service Configuration (service config) is a configuration
        language for configuring a gRPC service to become a user-facing product.
        The service config is simply the YAML representation of the
        ``google.api.Service`` proto message.

        As an alternative to annotating your proto file, you can configure gRPC
        transcoding in your service config YAML files. You do this by specifying
        a ``HttpRule`` that maps the gRPC method to a REST endpoint, achieving
        the same effect as the proto annotation. This can be particularly useful
        if you have a proto that is reused in multiple services. Note that any
        transcoding specified in the service config will override any matching
        transcoding configuration in the proto.

        Example:

        ::

            http:
              rules:
                # Selects a gRPC method and applies HttpRule to it.
                - selector: example.v1.Messaging.GetMessage
                  get: /v1/messages/{message_id}/{sub.subfield}

        ## Special notes

        When gRPC Transcoding is used to map a gRPC to JSON REST endpoints, the
        proto to JSON conversion must follow the `proto3
        specification <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.

        While the single segment variable follows the semantics of `RFC
        6570 <https://tools.ietf.org/html/rfc6570>`__ Section 3.2.2 Simple
        String Expansion, the multi segment variable **does not** follow RFC
        6570 Section 3.2.3 Reserved Expansion. The reason is that the Reserved
        Expansion does not expand special characters like ``?`` and ``#``, which
        would lead to invalid URLs. As the result, gRPC Transcoding uses a
        custom encoding for multi segment variables.

        The path variables **must not** refer to any repeated or mapped field,
        because client libraries are not capable of handling such variable
        expansion.

        The path variables **must not** capture the leading "/" character. The
        reason is that the most common use case "{var}" does not capture the
        leading "/" character. For consistency, all path variables must share
        the same behavior.

        Repeated message fields must not be mapped to URL query parameters,
        because no client library can support such complicated mapping.

        If an API needs to use a JSON array for request or response body, it can
        map the request or response body to a repeated field. However, some gRPC
        Transcoding implementations may not support this feature.

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
