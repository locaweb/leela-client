#!/usr/bin/python
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
import psutil
from time import sleep
from leela.machete import Acct

def cpu():
    c = psutil.cpu_times()
    client = Acct('Cpu')
    used = c.user + c.system + c.nice
    client.add('used', used)
    client.add('user', c.user)
    client.add('system', c.system)
    client.add('nice', c.nice)
    client.add('idle', c.idle)
    client.send()

def load():
    five, ten, fifteen = os.getloadavg()
    client = Acct('Load')
    client.add('5 min', five)
    client.add('10 min', ten)
    client.add('15 min', fifteen)
    client.send()

def memory():
    client = Acct('Memory')
    client.add('phymem_usage', psutil.phymem_usage().used / 1024 / 1024)
    client.add('virtmem_usage', psutil.virtmem_usage().used / 1024 / 1024)
    client.send()

def disk():
    client = Acct('Disk')
    for p in psutil.disk_partitions():
        u = psutil.disk_usage(p.mountpoint)
        client.add(p.mountpoint, u.percent)
    client.send()

def network():
    client = Acct('Network')
    nw = psutil.network_io_counters()
    client.add('bytes_sent', nw.bytes_sent)
    client.add('bytes_recv', nw.bytes_recv)
    client.add('packets_sent', nw.packets_sent)
    client.add('packets_recv', nw.packets_recv)
    client.send()

if __name__ == '__main__':
    while True:
        cpu()
        load()
        memory()
        disk()
        network()
        sleep(10)
