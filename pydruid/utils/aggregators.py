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

from filters import Filter

def longsum(raw_metric):
    return {"type": "longSum", "fieldName": raw_metric}


def doublesum(raw_metric):
    return {"type": "doubleSum", "fieldName": raw_metric}


def min(raw_metric):
    return {"type": "min", "fieldName": raw_metric}


def max(raw_metric):
    return {"type": "max", "fieldName": raw_metric}


def count():
    return {"type": "count"}


def hyperunique(raw_metric):
    return {"type": "hyperUnique", "fieldName": raw_metric}


def javascript(field_names, fn_aggregate, fn_combine, fn_reset):
    return {"type": "javascript",
            "fieldNames": field_names,
            "fnAggregate": fn_aggregate,
            "fnCombine": fn_combine,
            "fnReset": fn_reset}


def cardinality(field_names, by_row=False):
    return {"type": "cardinality",
            "fieldNames": field_names,
            "byRow": by_row}


def filtered(filter, aggregator):
    return {"type": "filtered",
            "filter": Filter.build_filter(filter),
            "aggregator": build_aggregators(aggregator)[0]}


def build_aggregators(agg_input):
    return [dict([('name', k)] + v.items())
            for (k, v) in agg_input.iteritems()]
