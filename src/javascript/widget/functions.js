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

  var fst = function (xs) {
    return(xs[0]);
  };

  var snd = function (xs) {
    return(xs[1]);
  };

  var datapoint_timestamp = fst;

  var datapoint_value = snd;

  var foldl = function (xs, z, f) {
    for (var k in xs) {
      if (xs.hasOwnProperty(k))
        z = f(xs[k], z);
    }
    return(z);
  };

  var id = function (x) {
    return(x);
  };

  var cons = function (x, xs) {
    xs.push(x);
    return(xs);
  };

  var snoc = function (x, xs) {
    xs.unshift(x);
    return(xs);
  };

  var map = function (xs, f) {
    return(foldl(xs, [], function (x, z) {
      return(snoc(f(x), z));
    }));
  };

  var sum = function (xs) {
    return(foldl(xs, 0, function (x, z) {
      return(x + z);
    }));
  };

  var min = function (xs) {
    return(foldl(xs, undefined, function (x, z) {
      if (z === undefined)
        return(x);
      else
        return(x>z ? z : x);
    }));
  };

  var max = function (xs) {
    return(foldl(xs, undefined, function (x, z) {
      if (z === undefined)
        return(x);
      else
        return(x>z ? x : z);
    }));
  };

  var _group = function (resolution, zero, datapoints) {
    var g = [];
    var r = [];
    var z = undefined;
    var s = 60;

    var process = function (d) {
      g.push(d);
      if (g.length == resolution) {
        r.push([datapoint_timestamp(g[0]), (sum(map(g, snd)) / resolution)]);
        g = [];
      }
      return(g);
    };

    for (var k in datapoints) {
      if (datapoints.hasOwnProperty(k)) {
        var d = datapoints[k];
        var t = datapoint_timestamp(d);
        var v = datapoint_value(d);
        z = (z === undefined ? t : z + s);
        while (z !== t) {
          process([z, zero]);
          z += s;
        }
        process([t, v]);
      }
    }
    if (g.length > 0)
      r.push([datapoint_timestamp(g[0]), (sum(map(g, snd)) / resolution)]);

    return(r);
  };

  var average = function (resolution, zero) {
    var f = function (json) {
      for (var m in json.results) {
        if (json.results.hasOwnProperty(m)) {
          json.results[m].series = _group(resolution, zero, json.results[m].series);
        }
      }
      return(json);
    };
    return(f);
  };

  var fmt_engeeringscale = function (n, units) {
    while (n>512 && units.length>1) {
      n = n / 1024.0;
      units.shift();
    }
    return([n, units[0]]);
  };

  var getprop = function (o, path, def) {
    var tmp = o;
    for (var k=0; k<path.length; k+=1) {
      if (tmp!==undefined && tmp.hasOwnProperty(path[k]))
        tmp = tmp[path[k]];
      else
        return(def);
    }
    return(tmp);
  };

  var dot = function (f, g) {
    var h = function () {
      var to_a = Array.prototype.slice;
      return(f(g.apply(null, to_a.call(arguments))));
    };
    return(h);
  };

  return({ average: average,
           min: min,
           max: max,
           map: map,
           snd: snd,
           fst: fst,
           dot: dot,
           getprop: getprop,
           id: id,
           fmt_engeeringscale: fmt_engeeringscale
         });

})();
