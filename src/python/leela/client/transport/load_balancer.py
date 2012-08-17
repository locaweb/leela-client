#!/usr/bin/python
# -*- coding: utf-8; -*-
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

def select(e, servers):
    h = hash(e.name())
    l = len(servers)
    return(servers[h % l])

def group(es, servers, maxsize=512):
    result = {}
    cursz  = 0
    for e in es:
        l = len(e.serialize())
        k = select(e, servers)
        if (k not in result):
            result[k] = [[]]
        if ((cursz+l) >= maxsize):
            cursz = 0
            result[k].insert(0, [])
        cursz += l
        result[k][0].append(e)
    return(result)
