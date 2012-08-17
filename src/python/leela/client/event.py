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

import time

SRV_TIMESTAMP = -1
CUR_TIMESTAMP = -2

def serialize_list(events):
    return("".join(map(lambda e: e.serialize(), events)))

class Event(object):
    """
    Raw event.
    """

    def __init__(self, name, value, timestamp=CUR_TIMESTAMP):
        self.n = name
        self.v = value
        if (timestamp == CUR_TIMESTAMP):
            self.t = time.time()
        elif (timestamp == SRV_TIMESTAMP):
            self.t = None
        else:
            self.t = timestamp

    def name(self):
        return(self.n)

    def value(self):
        return(self.v)

    def add_prefix(self, p):
        self.n = p + self.n
        return(self)

    def set_name(self, n):
        self.n = n
        return(self)

    def timestamp(self, t):
        self.t = t

    def serialize(self, precision=24):
        n = self.n
        v = float(self.v)
        t = self.t

        if (n is None):
            raise(RuntimeError("name must not be None"))

        if (t is None):
            fmtstr = "%%s: %%.%.df\n" % precision
            return(fmtstr % (n, v))
        else:
            fmtstr = "%%s: %%.%.df %%d\n" % precision
            return(fmtstr % (n, v, t))

    def __str__(self):
        return(unicode(self).encode("utf-8"))

    def __unicode__(self):
        return(self.serialize())

    def __hash__(self):
        return(hash(self.n))

    def __cmp__(self, o):
        if (self.n == o.n):
            return(cmp(self.t, o.t))
        return(cmp(self.n, o.n))
