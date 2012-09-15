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

from leela.client import event
from leela.client import functions as f
import time

def debug(s):
    s.measure()
    time.sleep(1)
    for e in s.measure():
        print(e.serialize())

class Sensor(object):

    class Value(object):

        def __init__(self, label, value):
            self.label = label
            self.value = value

    def __init__(self, name):
        self.name = name

    def mkevent(self, name, *args, **kwargs):
        return(event.Event("%s.%s" % (self.name,name), *args, **kwargs))

    def compute(self, nstate):
        """
        Must receive a dict with the following format:
        key: [v0, v1, ..., vN],

        where key: string
              v_n: Sensor.Value
        """
        raise(RuntimeError("abstract event"))

class PercentileSensor(Sensor):
    """
    Computes how much each value contributes toward a total, as follows:
      * (current_value - past_value) / (current_total - past_total)
    """

    def __init__(self, name):
        super(PercentileSensor, self).__init__(name)
        self.state = None

    def compute(self, nstate):
        if (self.state is None):
            self.state = nstate
            return([])
        result = []
        for k in range(min(len(nstate), len(self.state))):
            lbs = map(lambda x: x.label, nstate[k])
            vs1 = map(lambda x: x.value, nstate[k])
            vs0 = map(lambda x: x.value, self.state[k])
            values = f.percentage(vs1, vs0)
            result.extend(map(f.uncurry(self.mkevent), zip(lbs, values)))
        self.state = nstate
        return(result)

# TODO: counter resets
# TODO: counter wraps
class RateSensor(Sensor):
    """
    Computes the rate in seconds, as follows:
      * (current_measure - past_measure) / elapsed_time

    The first time you execute this there is no measure, as there is
    no previous state. Make sure you execute this multiples times
    giving it a reasonable interval between each call.
    """

    def __init__(self, name):
        super(RateSensor, self).__init__(name)
        self.state = None

    def compute(self, nstate):
        if (self.state is None):
            self.state = (nstate, time.time())
            return([])
        ntime  = time.time()
        result = []
        for k in range(min(len(nstate), len(self.state[0]))):
            lb = nstate[k].label
            v1 = nstate[k].value
            v0 = self.state[0][k].value
            x1 = ntime
            x0 = self.state[1]
            ev = self.mkevent(lb, f.derive()(v1, v0, x1, x0))
            result.append(ev)
        self.state = (nstate, ntime)
        return(result)
