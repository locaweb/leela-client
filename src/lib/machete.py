# Copyright 2012 Juliano Martinez
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
#
# @author: Juliano Martinez

import os
import bz2
from gevent import socket

class Acct(object):
    def __init__(self, service, server='127.0.0.1', port=6968):
        self.server = (server, port)
        self.service = service
        self.data = []

    def add(self, name, value):
        self.data.append("%s|%f" % (name, value))

    def send(self):
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.connect(self.server)
        message = "%s|%s||" % (os.uname()[1] ,self.service)
        message += "||".join(self.data)
        sock.send(bz2.compress(message, 9))
