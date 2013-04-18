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
  module LoadBalancer
    extend self

    def group(ring, values)
      g = Hash[ ring.values.map {|x| [x, []]} ]
      values.each do |v|
        node = ring.select(v.key)
        g[node] << v
      end
      return(g)
    end

    def group_limit(ring, values, maxsize)
      g = {}
      c = 0
      group(ring, values).each do |k, vs|
        tmp = [[]]
        vs.each do |v|
          c += v.size
          if (c >= maxsize)
            c = v.size
            tmp << []
          end
          tmp[-1] << v
        end
        g[k] = tmp.select {|vs| vs.size > 0}
      end
      return(g)
    end
  end
end
