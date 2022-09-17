#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

import re
from requests import get


class Dump_Url:
    def __init__(self, url: str):
        self.url = url

    def run(self):
        try:
            response = requests.get(self.url).text
        except:
            pass

