#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

from requests import get
from bs4 import BeautifulSoup as Soup
from re import findall
from random import shuffle

from ..core.common import *
from ..core.exception import *
from domaineer.set_env import *

class CubDomain:
    def __init__(self):
        self.url = "https://www.cubdomain.com/domains-registered-by-date/"
        self.h = {"user-agent":"GoogleBot v3"}
        self.about = """info

\"\"\"
    This Server is serve domains by dates, you must inputting valid dat
e formats which is correct by this bot.

    Valid Formats:
      @ 10,08,2021 or 10,Aug,2021
      @ 10 08 2021 or 10 Aug 2021
      @ 10-08-2021 or 10-Aug-2021
      @ 10/08/2021 or 10/Aug/2021
\"\"\""""

    def count_pages(self, date=""):
        req = get(self.url+date+"/1",headers=self.h).text
        sc = Soup(req,'html.parser')
        pages = sc.find_all("a",{'class':'page-link'})
        return int(pages[len(pages)-2].get_text())

    def dump(self, date="", page="1", exts=[]):
        req = get(self.url+date+"/"+page,headers=self.h).text
        sc = Soup(req,'html.parser')
        sites = sc.find_all("div",{'class':'col-md-4'})
        data = []
        for site in sites:
            if exts != []:
                for ext in exts:
                    if findall(
                            r"("+ext.replace('.','\.')+r")$", 
                            site.get_text().replace("\n","")
                    ):
                        data += [site.get_text().replace("\n","")]
                    else:
                        pass

            else:
                data += [site.get_text().replace("\n","")]

        return data


class AllUrlInfo:
    def __init__(self,domain="com"):
        self.url = f"https://{domain}.all-url.info/"
        self.h = {'user-agent':'Googlebot V3'}
        self.about = """Info. This server is serve domain by extensions and
 almost there only top level domains exists. So if your choosen extensi
on is not exists, not my bussiness..

  \"\"\"
    Valid inputs:
      @ .com or .COM
      @ com or COM
      @ com. or COM.
  \"\"\"
"""

    def connect(self):
        try:
            req = get(self.url,headers=self.h)
            return [True,req.status_code,req.text]
        except:
            return [False]

    def count_pages(self, page=""):
        if page == "":
            req = get(self.url,headers=self.h).text
            sc = Soup(req,'html.parser')
            count = sc.find(id="u1168-4")
            count = count.find_all("a")
            return len(count)-1
        else:
            req = get(self.url+f"{page}/0/",headers=self.h).text
            sc = Soup(req,'html.parser')
            count = sc.find("td",{'rowspan':'2'})
            count = count.find_all("br")
            return int(count[1].get_text()
                       .replace("\n","")
                       .replace("\t","")
                       .replace(" ","")
            )

    def dump_site(self, inpage="1", atpage="0"):
        req = get(self.url+f"{inpage}/{atpage}/",headers=self.h).text
        sc = Soup(req,'html.parser')
        dump = sc.find("div",{'align':'center'})
        dump = dump.find_all("font")
        result = []
        for site in dump:
            result += [site.get_text()]
        return result


class daWhois:
    def __init__(self):
        self.url= "https://dawhois.com/site/index-1%s.html" % ("0"*10)
        self.about = "It serve domains by A-Z list and it slice by every page server provided."

    def get_page(self, page_chs : str) -> str:
        url = "https://dawhois.com/site/index-%s.html" % page_chs
        return url

    def get_maxpage(self):
        _resp = get(self.url)
        soup = Soup(_resp.text, 'html.parser')
        max_page = soup.find_all('a')[11:-7]
        return len(max_page)-1

    def grab(self, url : str) -> list:
        with open(getenv("wordlists")+"/useragent.txt") as fp:
            user_agents = fp.read().splitlines()

        shuffle(user_agents)
        header = {'user-agent' : user_agents[0]}
        try:
            _resp = get(url,headers=header)
        except Exception as e:
            raise ServerConnectionError(e)
        finally:
            result = []
            soup = Soup(_resp.text, 'html.parser')
            _a = soup.find_all('a')
            if ".." in _a[20].text:
                errMsg = "Max page exceed! You should check the request page again."
                raise MaxPageExceed(errMsg)

        for res in _a[11:-7]:
            if res != '':
                result += [res.text]
            else: pass

        return result
