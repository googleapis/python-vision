# Copyright 2020 Google
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

import os

import vision_batch_annotate_files_gcs

GCS_ROOT = "gs://cloud-samples-data/vision/"


def test_sample_batch_annotate_files_gcs(capsys):
    storage_uri = os.path.join(GCS_ROOT, "document_understanding/kafka.pdf")

    vision_batch_annotate_files_gcs.sample_batch_annotate_files(storage_uri=storage_uri)

    out, _ = capsys.readouterr()

    assert "Full text" in out
    assert "Block confidence" in out
