#!/bin/sh

cat src/javascript/widget/functions.js src/javascript/widget/widget.js src/javascript/widget/version.js |\
   java -jar src/scripts/yuicompressor-2.4.7.jar --type js -o src/javascript/widget/leela-widget.min.js
