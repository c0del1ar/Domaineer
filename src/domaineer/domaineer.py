#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

from lib.parse.cliparser import ArgParser

args = ArgParser()

def main():
    if args.url:
        print("url is %s" % args.url)
    else:
        pass
