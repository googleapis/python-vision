# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.vision.v1p1beta1",
    manifest={
        "Vertex",
        "BoundingPoly",
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

    x: int = proto.Field(
        proto.INT32,
        number=1,
    )
    y: int = proto.Field(
        proto.INT32,
        number=2,
    )


class BoundingPoly(proto.Message):
    r"""A bounding polygon for the detected image annotation.

    Attributes:
        vertices (MutableSequence[google.cloud.vision_v1p1beta1.types.Vertex]):
            The bounding polygon vertices.
    """

    vertices: MutableSequence["Vertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Vertex",
    )


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

    x: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    y: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    z: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
