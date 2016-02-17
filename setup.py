# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import setup


def get_version(fname='jones_complexity.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)

setup(
    name='jones-complexity',
    version=get_version(),
    description="Jones Complexity checker, plugin for flake8",
    long_description=get_long_description(),
    keywords='flake8',
    author='Rich Jones',
    author_email='rich@openwatch.net',
    url='https://github.com/Miserlou/JonesComplexity',
    license='Expat license',
    py_modules=['jones_complexity'],
    zip_safe=False,
    setup_requires=['nose'],
    tests_require=['nose'],
    entry_points={
        'flake8.extension': [
            'J901 = jones_complexity:JonesComplexityChecker',
            'J902 = jones_complexity:JonesComplexityChecker',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
