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

class DiskUsage(sensor.Sensor):

    def __init__(self):
        super(DiskUsage, self).__init__("du")

    def measure(self):
        result = []
        for d in psutil.disk_partitions():
            k    = d.mountpoint
            data = psutil.disk_usage(k)
            events = [ self.mkevent("%s.total" % (k,), data.total),
                       self.mkevent("%s.used" % (k,), data.used),
                       self.mkevent("%s.free" % (k,), data.free)]
            result.extend(events)
        return(result)

if (__name__ == "__main__"):
    sensor.debug(DiskUsage())
