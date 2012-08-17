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

from nose.tools import *
from leela.client.sensors.linux import load

def test_load_sensor_is_stateless():
    sensor = load.Load()
    ok_([] != sensor.measure())

def test_load_sensor_produces_core_metrics():
    sensor = load.Load()
    events = [e.name() for e in sensor.measure()]
    ok_("loadavg.1" in events)
    ok_("loadavg.5" in events)
    ok_("loadavg.15" in events)
