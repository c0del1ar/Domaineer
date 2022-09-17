#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

from bs4 import BeautifulSoup as Soup
from builtins import object
import re

class CMSDetector(object):
    def __init__(self, data):
        self.data = data
        self.app = self.process()
        self.app_url = self.apptourl()

    def process(self):
        apps = ""
        links = []
        meta_tests = {
            "Joomla":"/joomla/i",
            "vBulletin":"/vBulletin/i",
            "WordPress":"/wordPress/i",
            "XOOPS":"/xoops/i",
            "Plone":"/plone/i",
            "MediaWiki":"/MediaWiki/i",
            "CMSMadeSimple":"/CMS Made Simple/i",
            "SilverStripe":"/SilverStripe/i",
            "Movable Type":"/Movable Type/i",
            "Amiro.CMS":"/Amiro/i",
            "Koobi":"/koobi/i",
            "bbPress":"/bbPress/i",
            "DokuWiki":"/dokuWiki/i",
            "TYPO3":"/TYPO3/i",
            "PHP-Nuke":"/PHP-Nuke/i",
            "DotNetNuke":"/DotNetNuke/i",
            "Sitefinity":"/Sitefinity\s+(.*)/i",
            "WebGUI":"/WebGUI/i",
            "ez Publish":"/eZ\s*Publish/i",
            "BIGACE":"/BIGACE/i",
            "TypePad":"/typepad\.com/i",
            "Blogger":"/blogger/i",
            "PrestaShop":"/PrestaShop/i",
            "SharePoint":"/SharePoint/",
            "JaliosJCMS":"/Jalios JCMS/i",
            "ZenCart":"/zen-cart/i",
            "WPML":"/WPML/i",
            "PivotX":"/PivotX/i",
            "OpenACS":"/OpenACS/i",
            "phpBB":"/phpBB/i",
            "Serendipity":"/Serendipity/i",
            "Avactis":"/Avactis Team/i"
        }
        meta_env = Soup(self.data, 'html.parser').find_all("meta")
        for env in meta_env:
            for link in meta_tests:
                regexp = re.compile(meta_tests[link])
                if re.findall(regexp, str(env)):
                    apps = link
                else: pass

