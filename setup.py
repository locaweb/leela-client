#!/usr/bin/python
from distutils.core import setup

setup(name='python-leela',
    version='0.0.1',
    description='Collect and Chart anything',
    author='Juliano Martinez',
    author_email='juliano@martinez.io',
    url='https://github.com/ncode/python-leela',
    packages=['python-leela'],
    package_dir={'python-leela': 'src/lib'},
    data_files=[('/usr/share/python-leela/examples',
                    ['src/examples/cpu.py',
                     'src/examples/cpu.sh',
                     'src/examples/machine-status.py']
                )]
    )
