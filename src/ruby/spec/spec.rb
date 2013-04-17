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

require "minitest/spec"
require "minitest/autorun"

def randstr(size)
  alphabet = [("a".."z"),("A".."Z"),("0".."9")].map {|x| x.to_a}.flatten
  results  = []
  while (size > 0)
    tmp   = alphabet.shuffle.slice(0, size).join
    size -= tmp.size
    results << tmp
  end
  return(results.join)
end
