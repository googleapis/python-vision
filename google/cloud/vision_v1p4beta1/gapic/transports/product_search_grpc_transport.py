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

from google.cloud.vision_v1p4beta1.proto import product_search_service_pb2_grpc


class ProductSearchGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.vision.v1p4beta1 ProductSearch API.

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

        Wrapper message for ``int64``.

        The JSON representation for ``Int64Value`` is JSON string.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].CreateProductSet

    @property
    def list_product_sets(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_product_sets`.

        The next_page_token returned from a previous List request, if any.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListProductSets

    @property
    def get_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.get_product_set`.

        The ``Status`` type defines a logical error model that is suitable
        for different programming environments, including REST APIs and RPC
        APIs. It is used by `gRPC <https://github.com/grpc>`__. Each ``Status``
        message contains three pieces of data: error code, error message, and
        error details.

        You can find out more about this error model and how to work with it in
        the `API Design Guide <https://cloud.google.com/apis/design/errors>`__.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].GetProductSet

    @property
    def update_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.update_product_set`.

        For extensions, this is the name of the type being extended. It is
        resolved in the same manner as type_name.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].UpdateProductSet

    @property
    def delete_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.delete_product_set`.

        Permanently deletes a ProductSet. Products and ReferenceImages in the
        ProductSet are not deleted.

        The actual image files are not deleted from Google Cloud Storage.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].DeleteProductSet

    @property
    def create_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.create_product`.

        A user-supplied resource id for this Product. If set, the server
        will attempt to use this value as the resource id. If it is already in
        use, an error is returned with code ALREADY_EXISTS. Must be at most 128
        characters long. It cannot contain the character ``/``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].CreateProduct

    @property
    def list_products(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_products`.

        The ``Celebrity`` that this face was matched to.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListProducts

    @property
    def get_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.get_product`.

        Response message for the ``ListProductsInProductSet`` method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].GetProduct

    @property
    def update_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.update_product`.

        The resource type. It must be in the format of
        {service_name}/{resource_type_kind}. The ``resource_type_kind`` must be
        singular and must not include version numbers.

        Example: ``storage.googleapis.com/Bucket``

        The value of the resource_type_kind must follow the regular expression
        /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and
        should use PascalCase (UpperCamelCase). The maximum number of characters
        allowed for the ``resource_type_kind`` is 100.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].UpdateProduct

    @property
    def delete_product(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.delete_product`.

        Permanently deletes a product and its reference images.

        Metadata of the product and all its images will be deleted right away, but
        search queries against ProductSets containing the product may still work
        until all related caches are refreshed.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].DeleteProduct

    @property
    def create_reference_image(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.create_reference_image`.

        Creates and returns a new ProductSet resource.

        Possible errors:

        -  Returns INVALID_ARGUMENT if display_name is missing, or is longer
           than 4096 characters.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].CreateReferenceImage

    @property
    def delete_reference_image(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.delete_reference_image`.

        Permanently deletes a reference image.

        The image metadata will be deleted right away, but search queries
        against ProductSets containing the image may still work until all related
        caches are refreshed.

        The actual image files are not deleted from Google Cloud Storage.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].DeleteReferenceImage

    @property
    def list_reference_images(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_reference_images`.

        Request message for the ``ListProducts`` method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListReferenceImages

    @property
    def get_reference_image(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.get_reference_image`.

        Recognition confidence. Range [0, 1].

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].GetReferenceImage

    @property
    def add_product_to_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.add_product_to_product_set`.

        A developer-facing error message, which should be in English. Any
        user-facing error message should be localized and sent in the
        ``google.rpc.Status.details`` field, or localized by the client.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].AddProductToProductSet

    @property
    def remove_product_from_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.remove_product_from_product_set`.

        Removes a Product from the specified ProductSet.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].RemoveProductFromProductSet

    @property
    def list_products_in_product_set(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.list_products_in_product_set`.

        Required. The project OR ProductSet from which Products should be
        listed.

        Format: ``projects/PROJECT_ID/locations/LOC_ID``

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ListProductsInProductSet

    @property
    def import_product_sets(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.import_product_sets`.

        End-line hyphen that is not present in text; does not co-occur with
        ``SPACE``, ``LEADER_SPACE``, or ``LINE_BREAK``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].ImportProductSets

    @property
    def purge_products(self):
        """Return the gRPC stub for :meth:`ProductSearchClient.purge_products`.

        Maximum number of results of this type. Does not apply to
        ``TEXT_DETECTION``, ``DOCUMENT_TEXT_DETECTION``, or ``CROP_HINTS``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["product_search_stub"].PurgeProducts
