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

require "resolv"

DEFAULT_PORT = 6968

module LeelaClient
  module Api
    extend self

    def transport(servers)
      servers = servers.map do |addr|
        host, port = addr.split(":", 2)
        [Resolv.getaddress(host), (port || 6968).to_i]
      end

      UDPTransport.new MD5Ring.from_list(servers)
    end
  end
end
