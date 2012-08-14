#!/usr/bin/python
# -*- coding: utf-8; -*-

import os
from setuptools import find_packages
from setuptools import setup

def find_datafiles(root, path_f):
    result = []
    for (root, dirname, files) in os.walk(root):
        tr_root = path_f(root)
        if (tr_root != False):
            result.append((tr_root, map(lambda f: os.path.join(root, f), files)))
    return(result)

accept_f = lambda f: reduce(lambda acc, p: acc or f.startswith(p), ("./etc", "./usr"), False)
path_f   = lambda f: accept_f(f) and f[1:] or False
setup(
    name             = "leela-client",
    version          = "0.0.1",
    description      = "Collect, Monitor and Analyze anything - client module",
    author           = "Diego Souza, Juliano Martinez",
    author_email     = "dsouza@c0d3.xxx",
    url              = "http://leela.readthedocs.org",
    namespace_packages = ["leela"],
    # install_requires = ["psutil", "dnspython"],
    packages         = find_packages("src/python"),
    package_dir      = {"": "src/python"},
    data_files       = find_datafiles(".", path_f))
