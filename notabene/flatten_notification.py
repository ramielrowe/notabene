# Copyright 2014 - Dark Secret Software Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

def flatten(data, result, prefix=""):
    """Take a json structure and convert it to a flattened
       list of (key, value) tuples. For example:

       {"foo": [ 
                   "sam",
                   "alice",
                   { 
                       "bob": 99,
                       "fred": 100
                   },
                   "zoo"
               ]
       }

       returns

       [("foo[0]", "sam"),
        ("foo[1]", "alice"),
        ("foo[2].bob", 99),
        ("foo[2].fred", 100),
        ("foo[3]]", "zoo)]
    """
    if type(data) is list:
        for index, item in enumerate(data):
            sub = "%s[%d]" % (prefix, index)
            flatten(item, result, prefix=sub)
        return
    elif type(data) is dict:
        for key, value in data.iteritems():
            if prefix:
                sub = "%s.%s" % (prefix, key)
            else:
                sub = key
            flatten(value, result, prefix=sub)
        return
    result.append((prefix, data))
