# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Setup file for python code install
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import platform

from pkg_resources import DistributionNotFound, get_distribution
from setuptools import find_packages
from setuptools import setup
from fleetx.version import fleetx_version


def python_version():
    """
    get python version
    """
    return [int(v) for v in platform.python_version().split(".")]


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


REQUIRED_PACKAGES = ['numpy>=1.10.0']
#REQUIRED_PACKAGES = ['paddlepaddle', 'numpy>=1.10.0']
#if get_dist('paddlepaddle') is None and get_dist(
#        'paddlepaddle-gpu') is not None:
#    REQUIRED_PACKAGES.remove('paddlepaddle')

packages = [
    'fleetx',
    'fleetx.applications',
    'fleetx.dataset',
    'fleetx.utils',
]

package_dir = {
    'fleetx': './fleetx',
    'fleetx.applications': './fleetx/applications',
    'fleetx.dataset': './fleetx/dataset',
    'fleetx.utils': './fleetx/utils'
}

setup(
    name='fleet-x',
    version=fleetx_version.replace('-', ''),
    description=(''),
    long_description='',
    url='https://github.com/PaddlePaddle/Fleet',
    author='PaddlePaddle Author',
    author_email='paddle-dev@baidu.com',
    install_requires=REQUIRED_PACKAGES,
    packages=packages,
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': ['fleetsub = fleetx.utils.submitter:submitter']
    },
    license='Apache 2.0',
    keywords=('paddlepaddle distributed-training deep-learning'))
