#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by EtcAug10 a.k.a Arya Kresna and it is licensed
"""


from re import findall
from datetime import date,timedelta
from time import sleep
import json, socket
from requests import get
from config import *
from random import shuffle
from tqdm import tqdm


def grabber(server=""):
  import tool.grab as grab
  
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
          
          for page in tqdm(range(1,(totalpage+1)),f"{prefix} Grabbbing"):
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
    
    for homepage in tqdm(range(1,(pagef+1)),f"{prefix}Load page"):
      pagel = grab.count_pages(str(homepage))
      print(f"{prefix}Getting total of {str(pagel)} pages including datas in page {str(homepage)}.")
    
      for datapage in tqdm(range(0,pagel),f"{prefix} Grabbing"):
        datares = grab.dump_site(str(homepage),str(datapage))
        
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
  import tool.reverseip as revip
  
  if server == "1":
    reversing = revip.OsintSH()
    print(f"{prefix}@ Start using service 1")
    
    try:
      
      for ip in ip_addr:
        reversing.get_data(socket.gethostbyname(ip),useragent)
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
    reversing = revip.SonarOmnisintIO()
    print(f"{prefix}@ Start using service 2")
    
    try:
      
      for ip in ip_addr:
        reversing.get(socket.gethostbyname(ip))
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
    print(f"\n{revip.__about__}")
    inputting = False
    
    while inputting == False:
    
      try:
        ips,inputting = (open(input(f"{Color.blue}{prefix}? IPs from your list: {Color.default}"),"r").read().splitlines(),True)
      
      except Exception: print(f"{Color.red}{prefix}x No data found on your inputted file")
      
      except KeyboardInterrupt: quit(f"{prefix} Cancelling..")
      
    check = 1
    
    if check == 1:
      print(f"{prefix}i Checking connection availability in service 1")
      conn = revip.OsintSH()
      conn.get_data(ips[0])
      
      if len(conn.dump()) != 0:
        reverseip("1",ips)
      
      else: check = 2
          
    if check == 2:
      print(f"{prefix}i Checking connection availability in service 2")
      conn = revip.SonarOmnisintIO()
      conn.get(ips[0])
      
      try:
        
        if len(conn.dump()) != 0:
          reverseip("2",ips)
      
        else: check = 3
        
      except: check = 3
      
    if check == 3:
      print(f"{Color.red}{prefix}x Servers is busy{Color.default}")
      

def cmsscanner(sites=[]):
  import tool.cmsscan as cmsscan
  
  if sites != []:
    
    for web in sites:
      
      if "http" in web or "://" in web:
        pass
        
      else:
        web = "https://"+web
        
      print(f"{prefix} Try to scanning {web}..")
        
      try:
        result = cmsscan.CMS_Detector(get(web).text)
      
      except Exception: 
        print(f"{Color.red}{prefix}x There was an error with this shit{Color.default}")
        result = ""
      
      except KeyboardInterrupt: quit(f"{Color.green}---_ Quitting.. :( _---{Color.default}")
        
      if result != "":
        
        if result.app[0] != "":
          print(f"{Color.green}{prefix}i Success..")
          print(f">> CMS : {result.app[0]}")
          print(">> Build links : ",end='',flush=True)
          
          if result.app[1] != []:
            
            for link in range(len(result.app[1])):
              
              if result.app[1][link] == result.app[1][(len(result.app[1])-1)]: print(result.app[1][link],flush=True)
                
              else: print(result.app[1][link]+", ",end='',flush=True)
              
          else: print(f"{Color.red}Nothing found..")
          
          print(f"{Color.green}>> CMS URL : {result.app_url}{Color.default}")
          
          try:
            data_result = json.loads(open("cmsscanlist.json","r").read())
            
          except:
            data_result = {}
            
          data_result[web] = result.app[0]
          open("cmsscanlist.json","w").write(json.dumps(data_result))
          
        else: print(f"{Color.red}{prefix}x It is not using any CMS{Color.default}")
          
      else: pass
      
    print(f"{prefix}@ Done it! saved in cmsscanlist.json")
    
  else:
    
    while sites == []:
      input_list = input(f"{Color.blue}{prefix}? Input your list file : {Color.default}")
      
      try:
        sites = open(input_list,"r").read().splitlines()
        
      except:
        print(f"{Color.red}{prefix}x I tried to open your file but it isn't here or there..{Color.default}")
        sites = []
        
    print(f"{prefix}@ Starting with basic scan")
    cmsscanner(sites=sites)
    
    
def gdorker(search_query="",useragents=[]):
  import tool.gse as gdork
  
  if search_query != "":
    
    if useragents != []:
      shuffle(useragents)
      req = gdork.dorking(search_query,useragents[0])
      
    else:
      req = gdork.dorking(search_query)
      
    for res in req:
      open("dorklist.txt","a").write(res+"\n")
      
    if len(req) == 0:  print(f"{Color.red}{prefix}x Sorry, this might be my fault. You get nothing..{Color.default}")
    
    elif len(req) < 10:  print(f"{Color.green}{prefix} Sis You only get {len(req)}. Have a nice day..{Color.default}")
      
    else: print(f"{Color.green}{prefix}i Success, take {len(req)} results from this query.{Color.default}")
    
    print(f"{prefix}@ Done it, saved in dorklist.txt")
    
  else:
    print(f"{Color.yellow}{prefix}i Info.\n{gdork.__about__}{Color.default}")
    
    try:
      search_query = input(f"{Color.blue}{prefix}? Your search query : {Color.default}")
      uagent = input(f"{Color.blue}{prefix}? Want to use User Agent incognito mode? (y/n): {Color.default}")
      
      if uagent.lower() == "y": gdorker(search_query=search_query,useragents=open("ua.txt","r").read().splitlines())
        
      else: gdorker(search_query=search_query)
      
    except KeyboardInterrupt:
      exit()
      
def fuzzing():
  import tool.urlfuzzer as fuzzer

  print(f"{Color.yellow}{prefix}i Info tool.\n{fuzzer.__about__}{Color.default}")
  target = input(f"{Color.blue}{prefix}? Input URL: {Color.default}")
  
  if "https" in target or "://" in target:
    pass
  else:
    target = "https://"+target
  
  print(f"{prefix}i If you want to print only status code(s) you want it, Type it (Separate with commas). Else, then empty it.")
  sc = input(f"{Color.blue}{prefix}? Input Status Code: {Color.default}").split(",")
  pathsrc = ""
  
  while pathsrc == "":
    pathsrc = input(f"{Color.blue}{prefix}? Input wordlist: {Color.default}")
    if open(pathsrc,'r').read():
      pass
    else:
      print(f"{Color.red}{prefix}x I found nothing on your file{Color.default}")
      pathsrc = ""
      
  fz = fuzzer.Fuzz(target)
  fz.getpath(fuzzer.makepath(pathsrc))
  fz.setcodes(sc)
  fz.search()
  print(f"{prefix}! Total request(s): {len(fz.paths)}, Total Found: {Color.green}{len(fz.pathfound)}{Color.default}, Not Found: {Color.red}{len(fz.pathnotfound)}{Color.default}")
