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
import psutil
from leela.client import event
from leela.client.sensors import sensor

class Network(sensor.RateSensor):

    def __init__(self):
        super(Network, self).__init__("network")

    def measure(self):
        return(self.compute(self._instrument()))

    def _instrument(self):
        labels = ("bytes_tx/s", "bytes_rx/s", "pkts_tx/s", "pkts_rx/s")
        result = []
        agg    = {}
        for (k, vs) in psutil.network_io_counters(True).iteritems():
            k1 = k.split(":")[0]
            if (k1 not in agg):
                agg[k1] = vs
            else:
                agg[k1] = map(lambda (a,b): a+b, zip(agg[k1], vs))
        for (k, vs) in agg.iteritems():
            events = map(lambda (k1, v): sensor.Sensor.Value("%s.%s" % (k,k1), v), zip(labels, vs))
            result.extend(events)
        return(result)
