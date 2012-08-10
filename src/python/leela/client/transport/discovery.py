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

import dns.resolver
import struct
import md5
import socket
from leela.client.transport import udp

factory = { "udp": udp.UDPTransport }

def resolve(host):
    return(socket.gethostbyname(host))

def discover(srv, proto):
    if (proto != "udp"):
        raise(RuntimeError("only udp for now"))
    rec = "_%s._%s.locaweb.com.br" % (srv, proto)
    servers = sorted([(resolve(s.target), s.port) for s in dns.resolver.query(srv, "SRV")])
    return(factory[proto](servers))
