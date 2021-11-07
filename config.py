#!/usr/bin/env python3

""" 
  Copyright (C) 2021 Semi-Auto bot tool 
  made by EtcAug10 a.k.a Arya Kresna and it is licensed
"""

class Color:
  gray = "\033[30;1m"
  red = "\033[31;1m"
  green = "\033[32;1m"
  yellow = "\033[33;1m"
  blue = "\033[34;1m"
  pink = "\033[35;1m"
  cyan = "\033[36;1m"
  white = "\033[37;1m"
  default = "\033[37;0m"
  
_version_ = "1.3.6.3"
_author_ = "c0del1ar"
_name_ = "Domaineer"

banner = ["""
        {}##
     ###
   ##    {}#####        {}Domaineer
   ##    {}#   ###      {}by EtcAug10         |
   ##    {}#     #####  {}Version {}{}      |
     ###          {}##{}                      |
        #######   {}##{}  This FREE tool is   |
                  {}##{}  Licensed            |
        {}############{} ________/_____/___/__/{}
""".format(Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.white,_version_,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.default),
"""
    {}###########
    #############
    ###         ###
    ###           ###     {}Domain Engineer
    {}###       {}##{}   ##     {}by EtcAug10
##  {}###     {}##      {}#
 {}## {}###   {}##       {}##
  {}## {}## {}##        {}###     {}v{}
   {}## ##        {}###
    {}##  {}#########            {}#
    {}####################    {}##
    #########################{}
""".format(Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.white,_version_,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.gray,Color.green,Color.default)]

prefix = "\u2699"

about = ["Domain Engineer or called as Domaineer is a tool to extract or dump any datas of domains in hole net lines.\n\nWhen you use this tool, It means you are accepting all of the Terms and Conditions in Ethical Hacker's guide book. Hope you've read it.","This bot helps you in doing penetration testing, learning the ins and outs of domains, analyzing objects, even doing stupid things like hacking your own domain and showing it off in front of your friends.","A wide variety of hacking tools are here, use them with great care. Don't worry, there is no backdoor logger here. The bot will continue to be updated if bugs and changes are found to improve the quality of the bot and update exploits"]

tool_choices = ["Grab Sites","Reverse IP","CMS Scanner","Google SE","DFuzzer","Domain to IP"]
