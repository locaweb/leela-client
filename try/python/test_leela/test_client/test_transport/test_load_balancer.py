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

from nose.tools import *
from leela.client.transport import load_balancer

def test_loadbalancer_is_using_simple_hashing_algorithm():
    # N.B.: relyaing on the fact that hash(n) == n for integers
    eq_(0, load_balancer.select(0, [0,1,2]))
    eq_(1, load_balancer.select(1, [0,1,2]))
    eq_(2, load_balancer.select(2, [0,1,2]))
    eq_(0, load_balancer.select(3, [0,1,2]))

def test_loadbalancer_groups_items():
    # N.B.: relyaing on the fact that hash(n) == n for integers
    result = load_balancer.group([0,1,2,3,4], [0,1,2], lambda _: 0)
    eq_([[0,3]], result[0])
    eq_([[1,4]], result[1])
    eq_([[2]], result[2])

def test_loadbalancer_groups_items_respecting_maxsize():
    # N.B.: relyaing on the fact that hash(n) == n for integers
    result = load_balancer.group([0,1,2,3,4], [0,1,2], lambda _: 1, 1)
    eq_([[0],[3]], result[0])
    eq_([[1],[4]], result[1])
    eq_([[2]], result[2])
