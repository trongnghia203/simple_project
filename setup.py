#!/usr/bin/env python3
"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
from setuptools import setup

setup(
    name='simple-project',
    version='1.1.0',  # Required
    description='A simple project to practice the packaging with setuptools/setup.py',  # Optional
    url='https://github.com/trongnghia203/simple_project',  # Optional
    author='Nghia Le',  # Optional
    author_email='nghia.le@gooddata.com',  # Optional
    packages=["simple_code"],  # Required
    python_requires='>=3.5, <4',  # Optional
    install_requires=['pyyaml'],  # Optional
    package_data={  # Optional
        'simple_code': ['config.yaml'],
    },
    entry_points={  # Optional
        'console_scripts': [
            'simple.py=simple_code.simple:run',
        ],
    },
)
