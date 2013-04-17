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

require "spec/speclib.rb"
require "ostruct"
require "leela_client"

describe LeelaClient::LoadBalancer do

  describe :group do

    it "should group things using ring services" do
      ring  = LeelaClient::MD5Ring.from_list(["foo", "bar"])
      keys  = (1..100).map { tmp = randstr(rand(10..255)); OpenStruct.new(:size => tmp.size, :key => tmp) }
      group = LeelaClient::LoadBalancer.group(ring, keys)
      assert(group.size == 2)
    end

  end

  describe :group_limit do

    it "should group things using ring and respect maxsize" do
      size  = 20
      ring  = LeelaClient::MD5Ring.from_list(["foo", "bar"])
      keys  = (1..100).map { tmp = randstr(rand(10..255)); OpenStruct.new(:size => tmp.size, :key => tmp) }
      group = LeelaClient::LoadBalancer.group_limit(ring, keys, size)
      group.size.must_equal(2)
      group.map do |k, vvs|
        assert(vvs.size >= 1)
        vvs.each {|vs| assert(vs.size == 1 || vs.inject(0) {|acc, v| v.size + acc} <= size)}
      end
    end

  end

end
