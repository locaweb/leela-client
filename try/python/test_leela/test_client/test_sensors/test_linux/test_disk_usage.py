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
from leela.client.sensors.linux import disk_usage

def test_disk_usage_sensor_is_stateless():
    sensor = disk_usage.DiskUsage()
    ok_([] != sensor.measure())

def test_disk_usage_sensor_produces_core_metrics():
    sensor = disk_usage.DiskUsage()
    events = [e.name() for e in sensor.measure()]
    ok_(reduce(lambda acc, e: acc or e.endswith(".total"), events, False))
    ok_(reduce(lambda acc, e: acc or e.endswith(".used"), events, False))
    ok_(reduce(lambda acc, e: acc or e.endswith(".free"), events, False))
