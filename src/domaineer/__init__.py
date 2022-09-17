#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib.core.settings import (
    APP_NAME,
    VERSION,
    AUTHOR,
    COPYRIGHT
)

__version__ = VERSION
__title__ = APP_NAME
__author__ = AUTHOR
__build__ = 0x001000
__copyright__ = COPYRIGHT

sys.dont_write_bytecode = True
