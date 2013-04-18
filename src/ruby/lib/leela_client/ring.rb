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

require "set"
require "digest/md5"

module LeelaClient
  class Ring
    def token(key)
      raise(RuntimeError.new "abstract method")
    end

    def add_token!(token, value)
      raise(RuntimeError.new "abstract method")
    end

    def rm_token!(token)
      raise(RuntimeError.new "abstract method")
    end

    def select(token)
      raise(RuntimeError.new "abstract method")
    end

    def values
      raise(RuntimeError.new "abstract method")
    end
  end

  class MD5Ring < Ring
    def self.from_list(values)
      ring  = MD5Ring.new
      step  = 2**128 / values.size
      token = 0
      Set.new(values).sort.each do |v|
        ring.add_token!(token, v)
        token += step
      end

      ring
    end

    def initialize
      @ring = {}
    end

    def token(key)
      Digest::MD5.hexdigest(key).to_i(16)
    end

    def add_token!(token, value)
      @ring[token] = value
    end

    def rm_token!(token)
      @ring.delete(token)
    end

    def values
      @ring.values
    end

    def select(value)
      self.select_(self.token(value))
    end

    def select_(token)
      k = @ring.keys.sort.select {|x| x < token}.last
      @ring[k]
    end
  end
end
