#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by c0del1ar a.k.a Arya Kresna and it is licensed
"""


from random import shuffle
from config import *
from tool.core import *



class Main():
  
  def __init__(self):
    self.logos()
    self.inputassign()
  
  def logos(self):
    shuffle(banner)
    shuffle(about)
    print(banner[0])
    print(about[0])
    
  def inputassign(self):
    print(f"\n\n{prefix}i Choose your need{Color.default}\n")
    for a in range(len(tool_choices)):
      print(f"    [{a+1}] {tool_choices[a]}")
      
    choose_a_tool = False

    while choose_a_tool == False:
      
      try:
        choices = input(f"{Color.blue}{prefix}? Your choice: {Color.default}")
        choose_a_tool = True
        
      except KeyboardInterrupt:
        quit(f"{Color.green}---_ Happy hacking 😎 _---{Color.default}")
        
      match choices:
        case "1": grabber()
        case "2": reverseip()
        case "3": cmsscanner()
        case "4": gdorker()
        case "5": fuzzing()
        case "6": domainip()
        case _: 
            print(f"{Color.red}{prefix}x Not found your choosen tool{Color.default}")
            choose_a_tool = False



if __name__ == '__main__':
  mainmenu = True
  
  while mainmenu == True:
    Main()
    mainback = input(f"{Color.blue}{prefix}?Do you want to go back to Main Menu? (y/n) : {Color.default}")
    
    if mainback.lower() == 'y':
      pass
      
    else:
      quit(f"{Color.green}---_ Happy hacking 😎 _---{Color.default}")
