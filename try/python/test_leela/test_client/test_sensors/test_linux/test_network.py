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
from leela.client.sensors.linux import network

def test_network_sensor_is_stateful():
    sensor = network.Network()
    ok_([] == sensor.measure())
    ok_([] != sensor.measure())

def test_network_sensor_produces_core_metrics():
    sensor = network.Network()
    sensor.measure()
    events = [e.name() for e in sensor.measure()]
    ok_(reduce(lambda acc, e: acc or e.endswith(".bytes_rx/s"), events, False))
    ok_(reduce(lambda acc, e: acc or e.endswith(".bytes_tx/s"), events, False))
    ok_(reduce(lambda acc, e: acc or e.endswith(".pkts_tx/s"), events, False))
    ok_(reduce(lambda acc, e: acc or e.endswith(".pkts_tx/s"), events, False))
