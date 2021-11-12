#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by c0del1ar a.k.a Arya Kresna and it is licensed
"""


from re import findall,search
from requests import get
from urllib.parse import unquote
from config import *


__about__ = "This tool allows you to find the keywords you are looking for. By entering your search query, this tool works by retrieving the link section of search results via Google Search Engine."
__version__ = "0.1"

def dorking(query,useragent=""):
  
  for dumpfrom in range(0,1000,100):
    
      try:
        
        if useragent != "":
          req = get(f"https://google.com/search?q={query}&start={dumpfrom}&num=100",headers={'user-agent':useragent}).text
          
        else:
          req = get(f"https://google.com/search?q={query}&start={dumpfrom}&num=100").text
          
      except Exception:
        quit(f"{Color.red}{prefix}x There has a problem with this fucking site{Color.default}")
        
      result = findall(r"href=\"\/url\?q\=(.*?)\&amp",req)
      data = []
      
      for res in result:
        
        if search(r"(accounts\.google|support\.google)",res): pass
        
        else:
          
          if findall(r"(search|ie|filter)",res):
            break
          
          else:
            data += [unquote(res)]
            
  return data
