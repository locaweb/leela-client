#!/usr/bin/python
from distutils.core import setup

setup(name='python-leela',
    version='0.0.1',
    description='Collect and Chart anything',
    author='Juliano Martinez',
    author_email='juliano@martinez.io',
    url='https://github.com/ncode/python-leela',
    packages=['leela'],
    install_requires=['gevent>=0.13.6'],
    package_dir={'leela': 'src/lib'},
    data_files=[('/usr/share/python-leela/examples',
                    ['src/examples/cpu.py',
                     'src/examples/cpu.sh',
                     'src/examples/machine-status.py']
                )]
    )
