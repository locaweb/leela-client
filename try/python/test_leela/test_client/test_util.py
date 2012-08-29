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
import time
from nose.tools import *
from leela.client.utils import RateLimit

def test_ratelimit_with_negative_ttls_expires_immediately():
    rl = RateLimit()
    rl.set("foobar", -1)
    ok_(rl.expired("foobar"))

def test_ratelimit_must_expires_according_to_ttl():
    rl = RateLimit()
    rl.set("foobar", 0.5)
    ok_(not rl.expired("foobar"))
    time.sleep(1)
    ok_(rl.expired("foobar"))
