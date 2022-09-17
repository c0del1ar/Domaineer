#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

class Scrap:
    def __init__(self, urls:list):
        self.urls = urls
        self.result = {
            'wp_login' : [],
            'wp_includes': [],
            'wp_contents': [],
            'wp_xmlrpc' : []
        }

    def wp_login(self):
        for url in self.urls:
            if '/wp-login.php' in url:
                self.result["wp_login"] += [url]
            else: pass

        return self.result

    def wp_includes(self):
        for url in self.urls:
            if '/wp-includes' in url:
                self.result["wp_includes"] += [url]
            else: pass

        return self.result

    def wp_content(self):
        for url in self.urls:
            if '/wp-content' in url:
                self.result["wp_contents"] += [url]
            else: pass

        return self.result

    def xmlrpc(self):
        for url in self.urls:
            if '/xmlrpc.php' in url:
                self.result["wp_xmlrpc"] += [url]
            else: pass

        return self.result

    def run_all_scan(self):
        self.wp_login()
        self.wp_includes()
        self.wp_content()
        self.xmlrpc()
