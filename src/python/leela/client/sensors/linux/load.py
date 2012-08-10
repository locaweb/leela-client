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

import os
from leela.client import event
from leela.client.sensors import sensor

class Load(sensor.Sensor):

    def __init__(self):
        super(Load, self).__init__("loadavg")

    def measure(self):
        (l1, l5, l15) = os.getloadavg()
        return([self.mkevent("1", l1),
                self.mkevent("5", l5),
                self.mkevent("15", l15)])

if (__name__ == "__main__"):
    sensor.debug(Load())
