/*jslint continue: true, vars: true, indent: 2*/

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

LEELA.f = (function () {
  "use strict";

  var fst = function (xs) {
    return (xs[0]);
  };

  var snd = function (xs) {
    return (xs[1]);
  };

  var foldl = function (xs, z, f) {
    var k;
    for (k in xs) {
      if (xs.hasOwnProperty(k)) {
        z = f(xs[k], z);
      }
    }
    return (z);
  };

  var id = function (x) {
    return (x);
  };

  // var cons = function (x, xs) {
  //   xs.push(x);
  //   return (xs);
  // };

  var snoc = function (x, xs) {
    xs.unshift(x);
    return (xs);
  };

  var map = function (xs, f) {
    return (foldl(xs, [], function (x, z) {
      return (snoc(f(x), z));
    }));
  };

  var sum = function (xs) {
    return (foldl(xs, 0, function (x, z) {
      return (x + z);
    }));
  };

  var min = function (xs) {
    return (foldl(xs, undefined, function (x, z) {
      if (z === undefined) {
        return (x);
      }
      return (x > z ? z : x);
    }));
  };

  var max = function (xs) {
    return (foldl(xs, undefined, function (x, z) {
      if (z === undefined) {
        return (x);
      }
      return (x > z ? x : z);
    }));
  };

  var mean = function (xs) {
    var ys = Array.prototype.slice.call(xs);
    ys.sort();
    var len = ys.length;
    var mid = Math.floor(len / 2);
    if (len % 2 === 0) {
      return ((ys[mid - 1] + ys[mid]) / 2);
    }
    return (ys[mid]);
  };

  var avg = function (xs) {
    return (sum(xs) / xs.length);
  };

  var group = function (samples, datapoints) {
    var g = [];
    var r = [];

    var process = function (d) {
      g.push(d);
      if (g.length === samples) {
        r.push(Array.prototype.slice.call(g));
        g = [];
      }
      return (g);
    };

    var k;
    for (k in datapoints) {
      if (datapoints.hasOwnProperty(k)) {
        var d = datapoints[k];
        var t = fst(d);
        var v = snd(d);
        process([t, v]);
      }
    }

    if (g.length > 0) {
      r.push(g);
    }

    return (r);
  };

  var summarize = function (g, samples) {
    var h = function (data) {
      return ([fst(data[0]), g(map(data, snd))]);
    };
    var f = function (json) {
      var m;
      for (m in json.results) {
        if (json.results.hasOwnProperty(m)) {
          json.results[m].series = map(group(samples, json.results[m].series), h);
        }
      }
      return (json);
    };
    return (f);
  };

  var fmt_engineeringscale = function (n, units) {
    while (n > 512 && units.length > 1) {
      n = n / 1024.0;
      units.shift();
    }
    return ([n, units[0]]);
  };

  var getprop = function (o, path, def) {
    var tmp = o;
    var k;
    for (k = 0; k < path.length; k += 1) {
      if (tmp !== undefined && tmp.hasOwnProperty(path[k])) {
        tmp = tmp[path[k]];
      } else {
        return (def);
      }
    }
    return (tmp);
  };

  var dot = function (f, g) {
    var h = function () {
      var to_a = Array.prototype.slice;
      return (f(g.apply(null, to_a.call(arguments))));
    };
    return (h);
  };

  return ({ summarize: summarize,
            average: function (samples) { return (summarize(avg, samples)); },
            min: min,
            max: max,
            mean: mean,
            avg: avg,
            map: map,
            snd: snd,
            fst: fst,
            dot: dot,
            getprop: getprop,
            id: id,
            fmt_engineeringscale: fmt_engineeringscale
          });

}());
