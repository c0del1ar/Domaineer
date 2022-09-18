#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

from __future__ import print_function

try:
    import sys

    sys.dont_write_bytecode = True

    from lib.core.common import banner
    from lib.parse.cliparser import ArgParser

except KeyboardInterrupt:
    import time
    errMsg = "Cancelled by user"
    sys.exit("\r%s - %s" % (time.strftime("%X"), errMsg))


def main():
    banner()
    args = ArgParser()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        raise

