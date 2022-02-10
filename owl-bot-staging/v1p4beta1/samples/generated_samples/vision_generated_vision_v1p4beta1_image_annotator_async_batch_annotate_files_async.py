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
# Generated code. DO NOT EDIT!
#
# Snippet for AsyncBatchAnnotateFiles
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-vision


# [START vision_generated_vision_v1p4beta1_ImageAnnotator_AsyncBatchAnnotateFiles_async]
from google.cloud import vision_v1p4beta1


async def sample_async_batch_annotate_files():
    # Create a client
    client = vision_v1p4beta1.ImageAnnotatorAsyncClient()

    # Initialize request argument(s)
    request = vision_v1p4beta1.AsyncBatchAnnotateFilesRequest(
    )

    # Make the request
    operation = client.async_batch_annotate_files(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END vision_generated_vision_v1p4beta1_ImageAnnotator_AsyncBatchAnnotateFiles_async]
