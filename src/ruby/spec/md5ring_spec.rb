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

require "spec/spec.rb"
require "leela_client"

describe LeelaClient::MD5Ring do

  it "should distribute evenly the tokens in the ring" do
    size  = 10
    nodes = (0..size).to_a
    ring  = LeelaClient::MD5Ring.from_list(nodes)
    space = {}
    total = 0
    rand(1000..10000).times do
      key        = ring.select(randstr(rand(1..255)))
      space[key] = space.fetch(key, 0) + 1
      total     += 1
    end
    total = total.to_f
    base  = (space.values.first / total)
    space.values.map {|v| (v / total).must_be_close_to(base, 0.1)}
  end

end
