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

    def group(ring, metrics)
      group = Hash[ ring.values.map {|x| [x, []]} ]
      metrics.each do |m|
        node = ring.select(m.key)
        group[node] << m
      end

      group
    end

    def group_limit(ring, metrics, maxsize)
      g1 = {}
      c  = 0

      group(ring, metrics).each do |k, ms|
        g1[k] = [[]]
        ms.each do |m|
          c += m.size
          g1[k][-1] << m
          if (c >= maxsize)
            c = 0
            g1[k] << []
          end
        end
      end

      g1
    end
  end
end
