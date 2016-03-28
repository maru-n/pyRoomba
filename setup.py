#!/usr/bin/env python
# coding: utf-8


from setuptools import setup, find_packages
from pyroomba import __author__, __version__

setup(
    name             = 'pyroomba',
    version          = __version__,
    description      = 'python class to controll Roomba.',
    author           = __author__,
    #url              = 'https://github.com/maru-n/pyStargazer.git',
    packages         = ['pyroomba'],
    test_suite       = 'test',
    requires         = ['pyserial', 'numpy'],
)
