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

import math
import time
from leela.client import event

class Memory(object):

    def measure(self):
        values = self._snapshot()
        return([event.Event("memory.%s" % k, v) for (k,v) in values.iteritems()])

    def _snapshot(self):
        tr = {"MemTotal:": "main.total",
              "MemFree:": "main.free",
              "Buffers:": "main.buffers",
              "Cached:": "main.cached",
              "SwapTotal:": "swap.total",
              "SwapFree:": "swap.free"
             }
        result = {}
        with file("/proc/meminfo", "r") as f:
            for l in f.readlines():
                tmp = l.split()
                if (len(tmp) > 2 and tmp[0] in tr and tmp[2] == "kB"):
                    result[tr[tmp[0]]] = long(tmp[1])*1024
        free   = sum(map(lambda s: result.get(s,0), ("main.free", "main.buffers", "main.cached")))
        total  = result.get("main.total", 0)
        wfree  = result.get("swap.free", 0)
        wtotal = result.get("swap.free", 0)
        result["main.used"] = max(0, total - free)
        result["swap.used"] = max(0, wtotal - wfree)
        return(result)
