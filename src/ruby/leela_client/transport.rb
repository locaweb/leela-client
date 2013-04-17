# -*- encoding: utf-8; -*-
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

module LeelaClient
  class UDPTransport
    MAXPAYLOAD = 1472

    def initialize(ring)
      @ring = ring
      @sock = UDPSocket.new
    end

    def serialize_list(metrics)
      metrics.map(&:serialize).join("")
    end

    def send(metrics)
      LoadBalander.group_limit(@ring, metrics, MAXPAYLOAD).each do |addr, mms|
        mms.each do |ms|
          sent = @sock.send(serialize_list(ms), 0, addr[0], addr[1])
          raise if (sent > MAXPAYLOAD)
        end
      end
    end
  end
end
