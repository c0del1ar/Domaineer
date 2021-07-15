#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by EtcAug10 a.k.a Arya Kresna and it is licensed
"""


from re import findall
from datetime import date,timedelta
from time import sleep
from random import shuffle
from config import *


def grabber(server=""):
  from tool import grab
  
  if server == "1":
    print(f"{Color.default}{prefix}@ Start using server 1")
    sleep(1)
    print(f"{Color.yellow}{prefix}i ",end="")
    
    for char in grab.Service1().about:
      print(char,end="",flush=True)
      sleep(0.005)
      
    print(Color.default)
    fromdate = grab.inputdate("From")
    untildate = grab.inputdate("Until")
    extension = []
    forext = False
    
    while forext == False:
      forext = input(f"{Color.blue}{prefix}? Interesting to targetting extension? (Y/n): {Color.default}")
      
      if forext == "Y" or forext == "y":
        forext,targeting = (True,True)
        
      elif forext == "N" or forext == "n":
        forext,targeting = (True,False)
        
      else:
        print(f"{Color.red}{prefix}! Wrong Input!{Color.default}")
        forext = False
        
    while targeting == True:
      print(f"{prefix}i Separate with space")
      extension,targeting = (input(f"{Color.blue}{prefix}? Which Extension? (example: .com .go.us): {Color.default}").split(" "), False)
    
    start_date = date(int(fromdate[2]),int(grab.monthstrtoint(fromdate[1])),int(fromdate[0]))
    end_date = date(int(untildate[2]),int(grab.monthstrtoint(untildate[1])),int(untildate[0]))
    delta = timedelta(days=1)
    print(f"{prefix}i Getting Result..")
    _exec = grab.Service1()
    
    try:
      
      while start_date <= end_date:
        datedump = start_date.strftime("%Y-%m-%d")
        datedump_str = grab.list_to_date(start_date.strftime("%d %m %Y").split(" "))
        
        try:
          
          totalpage = _exec.count_pages(datedump)
          print(f"{prefix} There are {str(totalpage)} pages in {datedump_str}")
          sleep(0.5)
          print(f"{prefix} Dumping all of them..")
          sleep(0.5)
          totalresult = []
          
          for page in range(1,(totalpage+1)):
            result = _exec.dump(datedump,str(page),extension)
            
            for res in result:
              open("grablist.txt","a").write(res+"\n")
              totalresult += [res]
              
          if 1 < len(totalresult) < 1000:
            print(f"{Color.green}{prefix} Ah.. Only {len(totalresult)} of datas you get it. But good.{Color.default}")
            
          elif len(totalresult) == 0:
            print(f"{Color.red}{prefix} Oh no.. There is no data you take it for {datedump_str}{Color.default}")
            
          else:
            print(f"{Color.green}{prefix} Great! getting total {len(totalresult)} of datas in {datedump_str}{Color.default}",end="")
            
        except Exception:
          print(f"{Color.red}{prefix}! Error while processing..{Color.default}")
          
          if totalresult:
            print(f"{Color.green}But you got {len(totalresult)} of datas in {datedump_str}.{Color.default}")
            
          else:
            print(f"{Color.red}Request's timeout in {datedump_str}. Pass it!{Color.default}")
          
        start_date += delta
    
    except KeyboardInterrupt:
      start_date,end_date = (1,0)
      print(f"\n{prefix} Cancelling..")
      exit()
      
    print(f"{prefix}@ Done it, result in grablist.txt")
    
  elif server == "2":
    print(f"{Color.default}{prefix}@ Start using server 2")
    print(f"{Color.yellow}{prefix}i ",end="")
    
    for char in grab.Service2().about:
      print(char,end="",flush=True)
      sleep(0.005)
      
    print(Color.default)
    choosen = False
    
    while choosen == False:
      extension = input(f"{Color.blue}{prefix}? Choose an extension: {Color.default}")
      
      if findall(r"( |\,|\-|\/)",extension):
        print(f"{Color.red}{prefix}! Only an extension you can choose!{Color.default}")
        choosen = False
        
      elif len(findall(r"(\.)",extension)) > 1:
        print(f"{Color.red}{prefix}! You can't choose for sub extension!{Color.default}")
        choosen = False
        
      else: choosen,extension = (True,extension.replace('.',""))
      
      print(f"{prefix}i Checking connection to server.. ",end="",flush=True)
      grab = grab.Service2(extension)
      connection = grab.connect()
    
      if connection[0] == False:
        print(f"{Color.red}Can't connect! choose another extension.{Color.default}")
        choosen = False
        from tool import grab
      
      else: choosen = True
      
    print(f"{Color.green}Great! Let's take the datas{Color.default}")
    pagef = grab.count_pages()
    
    for homepage in range(1,(pagef+1)):
      pagel = grab.count_pages(str(homepage))
      print(f"{prefix}Getting total of {str(pagel)} pages including datas in page {str(homepage)}.")
      
      for datapage in range(0,pagel):
        datares = grab.dump_site(str(homepage),str(datapage))
        print(f"{Color.green}{prefix}@ Taking {len(datares)} data results{Color.default}")
        
        for domain in datares:
          open("grablist.txt","a").write(domain+"\n")
          
    print(f"{prefix} Result saved in grablist.txt")
    
  else:
    
    while server == "":
      print(f"\n{grab.__info__}")
      a_server = input(f"{Color.blue}{prefix}? Then your choice is: {Color.default}")
      server = findall(r"(1|2)",a_server)
      
      if server:
        
        if server[0] == "1":
          grabber("1")
          
        else:
          grabber("2")
          
      else:
        print(f"{Color.red}{prefix}x incorrect input!{Color.default}")
        server = ""
  

def reverseip(server="",ip_addr=[],useragent=""):
  from tool import reverseip
  
  if server == "1":
    reversing = reverseip.OsintSH()
    print(f"{prefix}@ Start using service 1")
    
    try:
      
      for ip in ip_addr:
        reversing.get_data(ip,useragent)
        result = reversing.dump()
        
        for res in result:
          open("reverseiplist.txt","a").write(res+"\n")
          
        if len(result) > 10: print(f"{prefix}@ {ip} >> {Color.green}[{len(result)} datas]{Color.default}")
          
        else: print(f"{prefix}@ {ip} >> {Color.red}[{len(result)} datas]{Color.default}")
        
    except Exception:
      print(f"{Color.red}{prefix}x Error while requesting data to server.{Color.default}")
      
    except KeyboardInterrupt:
      print(f"{prefix} Cancelling..")
      
  elif server == "2":
    reversing = reverseip.SonarOmnisintIO()
    print(f"{prefix}@ Start using service 2")
    
    try:
      
      for ip in ip_addr:
        reversing.get(ip)
        result = reversing.dump()
        
        for res in result:
          open("reverseiplist.txt","a").write(res+"\n")
          
        if len(result) > 10: print(f"{prefix}@ {ip} >> {Color.green}[{len(result)} datas]{Color.default}")
        
        else: print(f"{prefix}@ {ip} >> {Color.red}[{len(result)} datas]{Color.default}")
        
    except Exception:
      print(f"{Color.red}{prefix}x Error while requesting data to server.{Color.default}")
      
    except KeyboardInterrupt:
      print(f"{prefix} Cancelling..")
      
  else:
    print(f"\n{reverseip.__about__}")
    inputting = False
    
    while inputting == False:
    
      try:
        ips,inputting = (open(input(f"{Color.blue}{prefix}? IPs from your list: {Color.default}"),"r").read().splitlines(),True)
      
      except Exception: print(f"{Color.red}{prefix}x No data found on your inputted file")
      
      except KeyboardInterrupt: quit(f"{prefix} Cancelling..")
      
    check = 1
    
    if check == 1:
      print(f"{prefix}i Checking connection availability in service 1")
      conn = reverseip.OsintSH()
      conn.get(ips[0])
      
      if len(conn.dump()) != 0:
        reverseip("1",ips)
      
      else: check = 2
          
    if check == 2:
      print(f"{prefix}i Checking connection availability in service 1")
      conn = reverseip.SonarOmnisintIO()
      conn.get(ips[0])
      
      if len(conn.dump()) != 0:
        reverseip("2",ips)
      
      else: pass
    
    
      
if __name__ == '__main__':
  print(banner)
  shuffle(about)
  print(about[0])
  print(f"\n\n{prefix}i Choose your need{Color.default}\n")
  
  for a in range(len(tool_choices)):
    print(f"    [{a+1}] {tool_choices[a]}")
    
  choose_a_tool = False

  while choose_a_tool == False:
    choices = input(f"{Color.blue}{prefix}? Your choice: {Color.default}")
    choose_a_tool = True
    
    if choices == "1":
      grabber()
      
    elif choices == "2":
      reverseip()
      
    else: 
      print(f"{Color.red}{prefix}x Not found your choosen tool{Color.default}")
      choose_a_tool = False
  