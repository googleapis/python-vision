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

import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.vision.v1p3beta1",
    manifest={
        "Vertex",
        "NormalizedVertex",
        "BoundingPoly",
        "NormalizedBoundingPoly",
        "Position",
    },
)


class Vertex(proto.Message):
    r"""A vertex represents a 2D point in the image.
    NOTE: the vertex coordinates are in the same scale as the
    original image.

    Attributes:
        x (int):
            X coordinate.
        y (int):
            Y coordinate.
    """

    x = proto.Field(proto.INT32, number=1)

    y = proto.Field(proto.INT32, number=2)


class NormalizedVertex(proto.Message):
    r"""A vertex represents a 2D point in the image.
    NOTE: the normalized vertex coordinates are relative to the
    original image and range from 0 to 1.

    Attributes:
        x (float):
            X coordinate.
        y (float):
            Y coordinate.
    """

    x = proto.Field(proto.FLOAT, number=1)

    y = proto.Field(proto.FLOAT, number=2)


class BoundingPoly(proto.Message):
    r"""A bounding polygon for the detected image annotation.

    Attributes:
        vertices (Sequence[~.geometry.Vertex]):
            The bounding polygon vertices.
        normalized_vertices (Sequence[~.geometry.NormalizedVertex]):
            The bounding polygon normalized vertices.
    """

    vertices = proto.RepeatedField(proto.MESSAGE, number=1, message="Vertex",)

    normalized_vertices = proto.RepeatedField(
        proto.MESSAGE, number=2, message="NormalizedVertex",
    )


class NormalizedBoundingPoly(proto.Message):
    r"""A normalized bounding polygon around a portion of an image.

    Attributes:
        vertices (Sequence[~.geometry.NormalizedVertex]):
            Normalized vertices of the bounding polygon.
    """

    vertices = proto.RepeatedField(proto.MESSAGE, number=1, message="NormalizedVertex",)


class Position(proto.Message):
    r"""A 3D position in the image, used primarily for Face detection
    landmarks. A valid Position must have both x and y coordinates.
    The position coordinates are in the same scale as the original
    image.

    Attributes:
        x (float):
            X coordinate.
        y (float):
            Y coordinate.
        z (float):
            Z coordinate (or depth).
    """

    x = proto.Field(proto.FLOAT, number=1)

    y = proto.Field(proto.FLOAT, number=2)

    z = proto.Field(proto.FLOAT, number=3)


__all__ = tuple(sorted(__protobuf__.manifest))
