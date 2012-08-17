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
from leela.client.sensors.linux import memory

def test_memory_sensor_is_stateless():
    sensor = memory.Memory()
    ok_([] != sensor.measure())

def test_memory_sensor_produces_core_metrics():
    sensor = memory.Memory()
    events = [e.name() for e in sensor.measure()]
    ok_("memory.total" in events)
    ok_("memory.free" in events)
    ok_("memory.used" in events)
    ok_("memory.cached" in events)
    ok_("memory.buffers" in events)
    ok_("memory.swap_free" in events)
    ok_("memory.swap_used" in events)
    ok_("memory.swap_total" in events)
