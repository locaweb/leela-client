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

import random
from nose.tools import *
from leela.client.event import Event

def test_event_hash_func():
    eq_(hash("foobar"), hash(Event("foobar", random.randint(0, 10))))

def test_event_cmp_func():
    t0 = random.randint(0, 10)
    t1 = random.randint(0, 10)
    a = Event("foobar", 0, t0)
    b = Event("foobar", 0, t1)
    ok_(a == a)
    ok_(b == b)
    ok_(cmp(a,b) == cmp(t0, t1))
