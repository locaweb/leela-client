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
require "leela_client"

def test_serialize(m)
  "#{m.type} #{m.key.size}|#{m.key} #{m.value} #{m.timestamp.to_f};".must_equal(m.serialize)
end

describe LeelaClient::Gauge do

  it "should serialize properly" do
    test_serialize(LeelaClient::Gauge.new("foobar", rand))
  end

end

describe LeelaClient::Absolute do

  it "should serialize properly" do
    test_serialize(LeelaClient::Absolute.new("foobar", rand))
  end

end

describe LeelaClient::Derive do

  it "should serialize properly" do
    test_serialize(LeelaClient::Derive.new("foobar", rand))
  end

end

describe LeelaClient::Counter do

  it "should serialize properly" do
    test_serialize(LeelaClient::Counter.new("foobar", rand))
  end

end
