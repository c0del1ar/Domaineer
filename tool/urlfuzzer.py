#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by c0del1ar a.k.a Arya Kresna and it is licensed
"""

from requests import get
from config import *


__about__ = "This tool is used to finding some interesting path or file inside directory of the websites. The bot will automatically found the path by creating request onto the server."

def codeColor(scode):
  
  if scode in range(100,200):
    return Color.cyan
  elif scode in range(200,300):
    return Color.green
  elif scode in range(300,400):
    return Color.blue
  elif scode in range(400,500):
    return Color.red
  elif scode in range(500,600):
    return Color.gray

def makepath(inputfile):
  files = []
  
  for file in open(inputfile,'r').read().splitlines():
    chars = ""
    
    for char in range(len(file)):
      
      if char == 0:
        if file[char] == "/": pass
        else: chars += file[char]
      else: chars += file[char]
      
    files += [chars]
    
  return files

class Fuzz:
  
  def __init__(self,url):
    self.url = url
    self.paths = []
    self.pathfound = []
    self.pathnotfound = []
    self.codes = ['']
    
  def search(self):
    
    for path in self.paths:
      
      try:
        req = get(self.url+"/"+path)
        sc = req.status_code
        
        if self.codes != ['']:
          
          if str(sc) in self.codes:
            self.pathfound += [path]
            print(f"{Color.green}{prefix}@{Color.default} data: {path} // {codeColor(sc)}{sc}{Color.default}")
          
          else:
            self.pathnotfound += [path]
        
        else:
          
          if sc in range(400,500):
            self.pathnotfound += [path]
          
          else:
            self.pathfound += [path]
          
          print(f"{Color.green}{prefix}@{Color.default} data: {path} // {codeColor(sc)}{sc}{Color.default}")
            
      except:
        print (f"{Color.red}{prefix}! Connection error. Pass it{Color.default}")
  
  def setcodes(self,codes=['']):
    self.codes = codes
    return self.codes
    
  def getpath(self,paths=[]):
    self.paths = paths
    return self.paths
