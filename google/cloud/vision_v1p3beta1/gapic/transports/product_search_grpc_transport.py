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


import google.api_core.grpc_helpers
from google.api_core import operations_v1

from google.cloud.vision_v1p3beta1.proto import product_search_service_pb2_grpc


class ProductSearchGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.vision.v1p3beta1 ProductSearch API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-vision",
    )

    def __init__(
        self, channel=None, credentials=None, address="vision.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "product_search_stub": product_search_service_pb2_grpc.ProductSearchStub(
                channel
            )
        }

        # Because this API includes a method that returns a
        # long-running operation (proto: google.longrunning.Operation),
        # instantiate an LRO client.
        self._operations_client = google.api_core.operations_v1.OperationsClient(
            channel
        )

    @classmethod
    def create_channel(
        cls, address="vision.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def create_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.create_product_set`.

        Image-specific score for this color. Value in range [0, 1].

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].CreateProductSet

    @property
    def list_product_sets(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_product_sets`.

        Additional information regarding long-running operations. In
        particular, this specifies the types that are returned from long-running
        operations.

        Required for methods that return ``google.longrunning.Operation``;
        invalid otherwise.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListProductSets

    @property
    def get_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.get_product_set`.

        Yaw angle, which indicates the leftward/rightward angle that the
        face is pointing relative to the vertical plane perpendicular to the
        image. Range [-180,180].

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].GetProductSet

    @property
    def update_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.update_product_set`.

        Metadata for the batch operations such as the current state.

        This is included in the ``metadata`` field of the ``Operation`` returned
        by the ``GetOperation`` call of the ``google::longrunning::Operations``
        service.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].UpdateProductSet

    @property
    def delete_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.delete_product_set`.

        The next_page_token returned from a previous List request, if any.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].DeleteProductSet

    @property
    def create_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.create_product`.

        Wrapper message for ``uint32``.

        The JSON representation for ``UInt32Value`` is JSON number.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].CreateProduct

    @property
    def list_products(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_products`.

        Required. Resource name of product to delete.

        Format is: ``projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID``

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListProducts

    @property
    def get_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.get_product`.

        The amount of green in the color as a value in the interval [0, 1].

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].GetProduct

    @property
    def update_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.update_product`.

        Manages long-running operations with an API service.

        When an API method normally takes long time to complete, it can be
        designed to return ``Operation`` to the client, and the client can use
        this interface to receive the real response asynchronously by polling
        the operation resource, or pass the operation resource to another API
        (such as Google Cloud Pub/Sub API) to receive the response. Any API
        service that returns long-running operations should implement the
        ``Operations`` interface so developers can have a consistent client
        experience.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].UpdateProduct

    @property
    def delete_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.delete_product`.

        Gets information associated with a Product.

        Possible errors:

        -  Returns NOT_FOUND if the Product does not exist.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].DeleteProduct

    @property
    def create_reference_image(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.create_reference_image`.

        A user-supplied resource id for the ReferenceImage to be added. If
        set, the server will attempt to use this value as the resource id. If it
        is already in use, an error is returned with code ALREADY_EXISTS. Must
        be at most 128 characters long. It cannot contain the character ``/``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].CreateReferenceImage

    @property
    def delete_reference_image(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.delete_reference_image`.

        The custom pattern is used for specifying an HTTP method that is not
        included in the ``pattern`` field, such as HEAD, or "*" to leave the
        HTTP method unspecified for this rule. The wild-card rule is useful for
        services that provide content to Web (HTML) clients.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].DeleteReferenceImage

    @property
    def list_reference_images(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_reference_images`.

        The request message for ``Operations.GetOperation``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListReferenceImages

    @property
    def get_reference_image(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.get_reference_image`.

        Lists products in an unspecified order.

        Possible errors:

        -  Returns INVALID_ARGUMENT if page_size is greater than 100 or less
           than 1.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].GetReferenceImage

    @property
    def add_product_to_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.add_product_to_product_set`.

        Request message for the ``CreateProductSet`` method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].AddProductToProductSet

    @property
    def remove_product_from_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.remove_product_from_product_set`.

        Request message for the ``ImportProductSets`` method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].RemoveProductFromProductSet

    @property
    def list_products_in_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_products_in_product_set`.

        Required. The project in which the ProductSet should be created.

        Format is ``projects/PROJECT_ID/locations/LOC_ID``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListProductsInProductSet

    @property
    def import_product_sets(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.import_product_sets`.

        The hostname for this service. This should be specified with no
        prefix or protocol.

        Example:

        service Foo { option (google.api.default_host) = "foo.googleapi.com";
        ... }

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ImportProductSets
