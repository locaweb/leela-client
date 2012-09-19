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
from leela.client import event
from leela.client.sensors import sensor

class Cpu(sensor.PercentileSensor):

    def __init__(self, everything=False):
        super(Cpu, self).__init__("cpu")
        self.everything = everything

    def measure(self):
        return(self.compute(self._instrument()))

    def _instrument(self):
        labels = ("user", "nice", "system", "idle", "iowait", "irq", "soft_irq", "steal", "guest")
        data = []
        with file("/proc/stat", "r") as f:
            for l in f.readlines():
                if (l.startswith("cpu")):
                    tmp = l.split()
                    k   = tmp[0]
                    if (not self.everything and (k != "cpu")):
                        continue
                    values = map(long, tmp[1:])
                    events = map(lambda (k1,v): sensor.Sensor.Value("%s.%s" % (k,k1), v), zip(labels, values))
                    data.append(events)
        return(data)
