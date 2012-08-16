// All Rights Reserved.
//
//    Licensed under the Apache License, Version 2.0 (the "License");
//    you may not use this file except in compliance with the License.
//    You may obtain a copy of the License at
//
//        http://www.apache.org/licenses/LICENSE-2.0
//
//    Unless required by applicable law or agreed to in writing, software
//    distributed under the License is distributed on an "AS IS" BASIS,
//    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//    See the License for the specific language governing permissions and
//    limitations under the License.

var LEELA;

if (LEELA === undefined) {
  LEELA = {};
}

if (LEELA.backend == undefined) {
  LEELA.backend = {};
}

LEELA.widget = function (root, opts) {

  var options   = opts || {};
  var backend_f = (options.backend || LEELA.backend.flotr2 || LEELA.backend.hicharts);
  var backend   = backend_f(jQuery(root).get(0));
  var data      = [];

  var merge = function (items) {
    var l = items.length;
    var r = {};
    for (var i=0; i<l; i+=1) {
      for (var k in items[i].results) {
        if (items[i].results.hasOwnProperty(k))
          r[k] = items[i].results[k];
      }
    }
    return({results: r});
  };

  var render = function (json) {
    data.push(json);
    backend.render(merge(data), { title: options.title || "leela widget",
                                  subtitle: options.subtitle || "Powered by locaweb",
                                  chart: options.chart,
                                  yaxis: options.yaxis,
                                  xaxis: options.xaxis
                                });
  };

  return({"render": render});
}
