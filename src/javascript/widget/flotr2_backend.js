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

if (LEELA.backend === undefined) {
  LEELA.backend = {};
}

LEELA.backend.flotr2 = function (root) {

  var cspline_i = function (x, xk_1, yk_1, xk, yk, xk1, yk1, xk2, yk2) {
    var t   = (x-xk) / (xk1 - xk);
    var t2  = t*t;
    var t3  = t2*t;
    var h00 = 2*t3 - 3*t2 + 1;
    var h10 = t3 - 2*t2 + t;
    var h01 = -2*t3 + 3*t2;
    var h11 = t3 - t2;
    var m0  = (yk1-yk)/(2*(xk1 - xk)) + (yk-yk_1)/(2*(xk-xk_1));
    var m1  = (yk2-yk1)/(2*(xk2 - xk1)) + (yk1-yk)/(2*(xk1-xk));
    var y   = h00*yk + h10*(xk1-xk)*m0 + h01*yk1 + h11*(xk1-xk)*m1;
    return([x, y]);
  };

  var chspline = function (data) {
    // http://en.wikipedia.org/wiki/Cubic_Hermite_spline
    var ndata = [];
    var len   = data.length;
    var res   = 25;
    var min   = LEELA.f.min(LEELA.f.map(data, LEELA.f.snd));
    var max   = LEELA.f.max(LEELA.f.map(data, LEELA.f.snd));
    
    for (var k=0; k<len-1; k+=1) {
      var x    = data[k][0];
      var xk_1 = (data[k-1] || [0])[0];
      var yk_1 = (data[k-1] || [0,0])[1];
      var xk   = data[k][0];
      var yk   = data[k][1];
      var xk1  = data[k+1][0];
      var yk1  = data[k+1][1];
      var xk2  = (data[k+2] || [0])[0];
      var yk2  = (data[k+2] || [0,0])[1];
      var s    = (xk1 - xk)/res;
      for (var u=0; u<res; u+=1) {
        x += s;
        var xy = cspline_i(x, xk_1, yk_1, xk, yk, xk1, yk1, xk2, yk2);
        ndata.push([xy[0], (xy[1]>max ? max : (xy[1]<min ? min : xy[1]))]);
      }
    }

    return(ndata);
  };

  var format_s = function (json, fmap) {
    var series = [];
    for (var k in json.results) {
      if (json.results.hasOwnProperty(k)) {
        series.push({ label: k,
                      data: fmap(json.results[k].series)
                    });
      }
    }
    return(series);
  };

  var build_options = function(options) {
    var myopts = { xaxis: { title: LEELA.f.getprop(options, ["xaxis", "title"]),
                            tickFormatter: LEELA.f.getprop(options, ["xaxis", "labels", "formatter"], LEELA.f.id)
                          },
                   yaxis: { autoscale: true,
                            title: LEELA.f.getprop(options, ["yaxis", "title"]),
                            tickFormatter: LEELA.f.getprop(options, ["yaxis", "labels", "formatter"], LEELA.f.id)
                          },
                   title: options.title,
                   subtitle: options.subtitle,
                   selection: { mode: "x"
                              },
                   legend: { position: "ne"
                           },
                 };
    return(myopts);
  };

  var render = function (json, options) {
    var type   = LEELA.f.getprop(options, ["chart", "type"], "spline");
    var series = (type==="spline" ? format_s(json, chspline) : format_s(json, LEELA.f.id));
    Flotr.draw(root, series, build_options(options));
  };

  return({"render": render});
}
