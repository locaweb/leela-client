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
import random
from nose.tools import *
from leela.client.sensors.sensor import PercentileSensor
from leela.client.sensors.sensor import RateSensor

def test_percentile_sensor_computes_percentages_correctly():
    s = PercentileSensor("test")
    z = random.randint(0, 100)
    y = random.randint(0, 100)
    n = random.randint(0, 100)
    m = random.randint(0, 100)

    s.compute([[PercentileSensor.Value("foo", z), PercentileSensor.Value("bar", y)]])
    events  = s.compute([[PercentileSensor.Value("foo", z+m), PercentileSensor.Value("bar", y+n)]])
    results = {"test.foo": m / float((y+z+m+n) - (y+z)),
               "test.bar": n / float((y+z+m+n) - (y+z)),
              }
    for e in events:
        eq_(results[e.name()], e.value())

def test_rate_sensor_computes_rates_correctly():
    s = RateSensor("test")
    z = random.randint(0, 100)
    y = z + random.randint(0, 100)

    s.compute([[RateSensor.Value("foo", z)]])
    time.sleep(0.1)
    t0      = s.state[1]
    events  = s.compute([[RateSensor.Value("foo", y)]])
    t1      = s.state[1]
    results = {"test.foo": (y-z)/(t1-t0)}
    for e in events:
        eq_(results[e.name()], e.value())
