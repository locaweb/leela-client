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

require "cgi"
require "net/http"
require "json"

module LeelaClient

  class Transport

    def initialize(ring)
      @ring = ring
    end

    def send(metrics, opts={:method => :udp})
      if (opts[:method] == :http)
        HTTPTransport.new(@ring, opts).send(metrics)
      elsif (opts[:method] == :udp)
        UDPTransport.new(@ring, opts).send(metrics)
      else
        raise(RuntimeError.new "unknown method: #{opts[:method]}")
      end
    end
  end

  class HTTPTransport

    def initialize(ring, opts)
      @ring = ring
      @opts = opts
    end

    def send(metrics)
      sent  = 0
      proto = @opts[:ssl] ? "https" : "http"
      port  = @opts[:port] || (opts[:ssl] ? 443 : 80)
      LeelaClient::LoadBalancer.group(@ring, metrics).each do |addr, ms|
        ms.each do |m|
          uri = URI("#{proto}://#{addr[1]}:#{port}/v1/" + ::CGI::escape(m.key))
          res = ::Net::HTTP.start(addr[1],
                                  uri.port,
                                  :use_ssl      => uri.scheme == "https",
                                  :open_timeout => @opts[:timeout] || 5,
                                  :read_timeout => @opts[:timeout] || 5,
                                  :ssl_timeout  => @opts[:timeout] || 5) do |http|
            req              = ::Net::HTTP::Post.new(uri.path)
            req.body         = ::JSON::dump(m.serialize_json)
            req.content_type = "application/json"
            http.request(req)
          end
          if (res.code.to_i == 201)
            sent += 1
          end
        end
      end
      return(sent)
    end
  end

  class UDPTransport
    MAXPAYLOAD   = 1472
    DEFAULT_PORT = 6968

    def initialize(ring, opts)
      @ring = ring
      @opts = opts
      @sock = UDPSocket.new
    end

    def serialize_list(metrics)
      metrics.map(&:serialize).join("")
    end

    def send(metrics)
      sent = 0
      LeelaClient::LoadBalancer.group_limit(@ring, metrics, MAXPAYLOAD).each do |addr, mms|
        mms.each do |ms|
          @sock.send(serialize_list(ms), 0, addr[0], @opts[:port] || DEFAULT_PORT)
          sent += ms.size # yeah, hopefully!
        end
      end
      return(sent)
    end
  end
end
