#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by c0del1ar a.k.a Arya Kresna and it is licensed
"""

from requests import get
from bs4 import BeautifulSoup
from re import findall
from config import Color,prefix


__info__ = "There are 2 servers we provided, which every server providing their own data.\n\nServer 1, serve domains by date registration.\nServer 2, serve domains by their extensions. So, choose it first."



class Service1:
  
  def __init__(self):
    self.url = "https://www.cubdomain.com/domains-registered-by-date/"
    self.h = {"user-agent":"GoogleBot v3"}
    self.about = """info

\"\"\"
    This Server is serve domains by dates, you must inputting valid date formats which is correct by this bot.
    
    Valid Formats:
      @ 10,08,2021 or 10,Aug,2021
      @ 10 08 2021 or 10 Aug 2021
      @ 10-08-2021 or 10-Aug-2021
      @ 10/08/2021 or 10/Aug/2021
\"\"\"
"""
  
  def count_pages(self,date=""):
    req = get(self.url+date+"/1",headers=self.h).text
    sc = BeautifulSoup(req,'html.parser')
    pages = sc.find_all("a",{'class':'page-link'})
    return int(pages[len(pages)-2].get_text())
    
  def dump(self,date="",page="1",exts=[]):
    req = get(self.url+date+"/"+page,headers=self.h).text
    sc = BeautifulSoup(req,'html.parser')
    sites = sc.find_all("div",{'class':'col-md-4'})
    data = []
    for site in sites:
      if exts != []:
        for ext in exts:
          if findall(r"("+ext.replace('.','\.')+r")$",site.get_text().replace("\n","")):
            data += [site.get_text().replace("\n","")]
          else:
            pass
      else:
        data += [site.get_text().replace("\n","")]
    return data



class Service2:
  
  def __init__(self,domain="com"):
    self.url = f"https://{domain}.all-url.info/"
    self.h = {'user-agent':'Googlebot V3'}
    self.about = """Info. This server is serve domain by extensions and almost there only top level domains exists. So if your choosen extension is not exists, not my bussiness..

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
      return [False,None,None]
      
  def count_pages(self,page=""):
    if page == "":
      req = get(self.url,headers=self.h).text
      sc = BeautifulSoup(req,'html.parser')
      count = sc.find(id="u1168-4")
      count = count.find_all("a")
      return len(count)-1
    else:
      req = get(self.url+f"{page}/0/",headers=self.h).text
      sc = BeautifulSoup(req,'html.parser')
      count = sc.find("td",{'rowspan':'2'})
      count = count.find_all("br")
      return int(count[1].get_text().replace("\n","").replace("\t","").replace(" ",""))
      
  def dump_site(self,inpage="1",atpage="0"):
    req = get(self.url+f"{inpage}/{atpage}/",headers=self.h).text
    sc = BeautifulSoup(req,'html.parser')
    dump = sc.find("div",{'align':'center'})
    dump = dump.find_all("font")
    result = []
    for site in dump:
      result += [site.get_text()]
    return result
      


def list_to_date(listin=[]):
  month_str = {"01":"Jan","02":"Feb","03":"Mar","04":"Apr","05":"May","06":"Jun","07":"Jul","08":"Aug","09":"Sep","10":"Oct","11":"Nov","12":"Dec"}
  month_int = ["01","02","03","04","05","06","07","08","09","10","11","12"]
  if listin[1] in month_int:
    month = listin[1].replace(listin[1],month_str[listin[1]])
  else:
    month = listin[1]
  return "".join(listin[0]+" "+month+" "+listin[2])
  

def monthstrtoint(string):
  chrs = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
  try:
    return chrs[string]
  except:
    return string


def inputdate(at,date=[]):
  while len(date) != 3:
    date = input(f"{Color.blue}{prefix}? {at} date: {Color.default}")
    if "," in date:
      date = date.split(",")
    elif " " in date:
      date = date.split(" ")
    elif "-" in date:
      date = date.split("-")
    elif "/" in date:
      date = date.split("/")
    else:
      pass
    if len(date) != 3:
      print(f"{Color.red}{prefix}! Error format!{Color.default}")
    else:
      if len(date[0]) != 2:
        print(f"{Color.red}{prefix}! Error format!{Color.default}")
        date = []
      elif len(date[1]) > 3:
        print(f"{Color.red}{prefix}! Error format!{Color.default}")
        date = []
      elif len(date[2]) != 4:
        print(f"{Color.red}{prefix}! Error format!{Color.default}")
        date = []
  if findall(r"(0).",date[0]):
    date[0] = date[0].replace("0","")
  if findall(r"(0).",date[1]):
    date[1] = date[1].replace("0","")
  return date
