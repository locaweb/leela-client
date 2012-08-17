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
from leela.client.sensors.linux import cpu

def test_cpu_sensor_is_stateful():
    sensor = cpu.Cpu()
    ok_(sensor.measure() == [])
    ok_(sensor.measure() != [])

def test_cpu_sensor_produces_core_metrics():
    sensor = cpu.Cpu()
    sensor.measure()
    sensor.measure()
    events = [e.name() for e in sensor.measure()]
    ok_("cpu.cpu.user" in events)
    ok_("cpu.cpu.nice" in events)
    ok_("cpu.cpu.system" in events)
    ok_("cpu.cpu.idle" in events)
    ok_("cpu.cpu0.user" in events)
    ok_("cpu.cpu0.nice" in events)
    ok_("cpu.cpu0.system" in events)
    ok_("cpu.cpu0.idle" in events)
