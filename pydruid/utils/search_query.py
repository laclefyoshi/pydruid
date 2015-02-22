#
# Copyright 2013 Metamarkets Group Inc.
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

try:
    import json
except ImportError:
    import simplejson as json
    pass


class SearchQuery:
    def __init__(self, **args):
        if args['type'] == 'insensitive_contains':
            self.search_query = {'query': {'type': 'insensitive_contains',
                                          'value': args['value']}}
        elif args['type'] == 'fragment':
            self.search_query = {'query': {'type': 'fragment',
                                           'values': args['values']}}
        else:
            raise NotImplementedError(
                'SearchQuery type: {0} does not exist'.format(args['type']))

    def show(self):
        print(json.dumps(self.search_query, indent=4))

    @staticmethod
    def build_search_query(query_obj):
        return query_obj.search_query['query']

