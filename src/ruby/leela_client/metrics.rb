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
  module Metric
    attr_reader :type
    attr_accessor :key
    attr_accessor :value
    attr_accessor :timestamp

    def serialize
      size  = @key.size
      now   = @timestamp.to_f.to_s
      if (@value.integer?)
        value = @value.to_f.to_s
      elsif (@value.nan?)
        value = "nan"
      elsif (@value.infinite? == 1)
        value = "inf"
      elsif (@value.infinite? == -1)
        value = "-inf"
      else
        value = @value.to_s
      end

      "#{@type} #{size}|#{@key} #{value} #{now};"
    end

    def size
      self.serialize.size
    end
  end

  class Gauge
    include Metric

    def initialize(key, value)
      @type      = "gauge"
      @key       = key
      @value     = value
      @timestamp = Time.now
    end

  end

  class Counter
    include Metric

    def initialize(key, value)
      @type      = "counter"
      @key       = key
      @value     = value
      @timestamp = Time.now
    end
  end

  class Derive
    include Metric

    def initialize(key, value)
      @type      = "derive"
      @key       = key
      @value     = value
      @timestamp = Time.now
    end
  end

  class Absolute
    include Metric

    def initialize(key, value)
      @type      = "absolute"
      @key       = key
      @value     = value
      @timestamp = Time.now
    end
  end
end
