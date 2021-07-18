#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by EtcAug10 a.k.a Arya Kresna and it is licensed
"""


from random import shuffle
from config import *
from tool.core import *
    
    
      
if __name__ == '__main__':
  shuffle(banner)
  print(banner[0])
  shuffle(about)
  print(about[0])
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
    
    if choices == "1":
      grabber()
      
    elif choices == "2":
      reverseip()
      
    elif choices == "3":
      cmsscanner()
      
    elif choices == "4":
      gdorker()
      
    else: 
      print(f"{Color.red}{prefix}x Not found your choosen tool{Color.default}")
      choose_a_tool = False
  