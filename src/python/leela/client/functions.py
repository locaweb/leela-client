6#!/usr/bin/python
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

def derive(zero=0.0, minimum=0.0):
    def f(y1, y0, x1, x0):
        dx = float(x1 - x0)
        if (dx == 0.0):
            return(zero)
        else:
            return(max(minimum, (y1-y0) / dx))
    return(f)

def fst(pair):
    return(pair[0])

def snd(pair):
    return(pair[1])

def uncurry(f):
    def g(args, **kwargs):
        return(f(*args, **kwargs))
    g.__name__ = f.__name__
    return(g)

def percentage(state1, state0):
    result = []
    xs1 = sum(state1)
    xs0 = sum(state0)
    return(map(lambda (y1,y0): derive()(y1, y0, xs1, xs0), zip(state1, state0)))
