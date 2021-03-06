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

import socket
from leela.client import event
from leela.client.transport import load_balancer
from leela.client.transport import interface

class UDPTransport(interface.Transport):

    def __init__(self, servers):
        self.l = list(sorted(servers))
        self.s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def probe(self):
        pass

    def send(self, es):
        f = lambda e: len(e.serialize())
        g = load_balancer.group(es, self.l, f)
        for (addr, ess) in g.iteritems():
            for es in ess:
                self.s.sendto(event.serialize_list(es), 0, addr)

    def send_event(self, e):
        addr = load_balancer.select(e, self.l)
        self.s.sendto(e.serialize(), 0, addr)
