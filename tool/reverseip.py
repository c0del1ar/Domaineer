#!/usr/bin/env python3


""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by EtcAug10 a.k.a Arya Kresna and it is licensed
"""

"""
  You can get this library tool in
  https://github.com/EtcAug10/ReverseIP
"""

from requests import Session,post,get
from re import match,findall
import json

__version__ = "1.0.7"
__name__ = "Reverse Ip Library"
__author__ = "Arya Kresna"
__about__ = "\nThis tool is used to perform domain extraction on the same IP service. Use in accordance with the terms and conditions that apply.\n"

class OsintSH:
  
  def __init__(self):
    self.url = "https://osint.sh/reverseip/"
    self.ip = ""
    self.ua = ""
    self.data = {'domain':self.ip}
  
  def get_data(self,ip,ua=""):
    self.ip = ip
    self.ua = ua
    self.data['domain'] = self.ip
  
  def dump(self):
    if self.ua != "":
      r = post(self.url,data=self.data,headers={"user-agent":self.ua})
    else:
      r = post(self.url,data=self.data)
    return findall(r"Domain\">(.*?)<\/",r.text.replace("\n","").replace(" ",""))

class SonarOmnisintIO:
  
  def __init__(self):
    self.url = "https://sonar.omnisint.io/reverse/"
    self.ip = ""
    self.headers = ""
  
  def get(self,ip,headers=""):
    self.ip = ip
    self.headers = headers
    return True
    
  def dump(self):
    req = get(self.url+self.ip,headers=self.headers).text
    return json.loads(req)