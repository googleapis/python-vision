#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to perform import product sets operations
on Product set in Cloud Vision Product Search.

For more information, see the tutorial page at
https://cloud.google.com/vision/product-search/docs/
"""

import argparse

# [START vision_product_search_tutorial_import]
from google.cloud import vision
# [END vision_product_search_tutorial_import]


# [START vision_product_search_import_product_images]
def import_product_sets(project_id, location, gcs_uri):
    """Import images of different products in the product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        gcs_uri: Google Cloud Storage URI.
            Target files must be in Product Search CSV format.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(
        project=project_id, location=location)

    # Set the input configuration along with Google Cloud Storage URI
    gcs_source = vision.types.ImportProductSetsGcsSource(
        csv_file_uri=gcs_uri)
    input_config = vision.types.ImportProductSetsInputConfig(
        gcs_source=gcs_source)

    # Import the product sets from the input URI.
    response = client.import_product_sets(
        parent=location_path, input_config=input_config)

    print('Processing operation name: {}'.format(response.operation.name))
    # synchronous check of operation status
    result = response.result()
    print('Processing done.')

    for i, status in enumerate(result.statuses):
        print('Status of processing line {} of the csv: {}'.format(
            i, status))
        # Check the status of reference image
        # `0` is the code for OK in google.rpc.Code.
        if status.code == 0:
            reference_image = result.reference_images[i]
            print(reference_image)
        else:
            print('Status code not OK: {}'.format(status.message))
# [END vision_product_search_import_product_images]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')
    parser.add_argument(
        '--project_id',
        help='Project id.  Required',
        required=True)
    parser.add_argument(
        '--location',
        help='Compute region name',
        default='us-west1')

    import_product_sets_parser = subparsers.add_parser(
        'import_product_sets', help=import_product_sets.__doc__)
    import_product_sets_parser.add_argument('gcs_uri')

    args = parser.parse_args()

    if args.command == 'import_product_sets':
        import_product_sets(args.project_id, args.location, args.gcs_uri)
