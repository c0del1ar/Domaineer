#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
"""

import os
import sys
from random import shuffle
from colorama import Fore

# about app
AUTHOR = "Arya Kresna"
VERSION = "0.1.3"
APP_NAME = "Domaineer"
COPYRIGHT = "Copyright (c) 2021 Domaineer"

# Directory paths
ABS_PATH = os.path.dirname(os.path.abspath('__file__'))
WEBSHELL_LIST = ABS_PATH + "/webshell"
WORDLIST = ABS_PATH + "/wordlists"

# about app
BANNER = ["""
        %s##
     ###
   ##    %s#####        %s%s
   ##    %s#   ###      %sby c0del1ar         |
   ##    %s#     #####  %sversion %s%s       |
     ###          %s##%s                      |
        #######   %s##%s  This FREE tool is   |
                  %s##%s  Licensed            |
        %s############%s ________/_____/___/__/%s
""" % (Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,APP_NAME,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.WHITE,
       VERSION,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.RESET),
"""
    %s###########
    #############
    ###         ###
    ###           ###     %s%s
    %s###       %s##%s   ##     %sby c0del1ar
##  %s###     %s##      %s#
 %s## %s###   %s##       %s##
  %s## %s## %s##        %s###     %sv%s
   %s## ##        %s###
    %s##  %s#########            %s#
    %s####################    %s##
    #########################%s
""" % (Fore.LIGHTBLACK_EX,
       APP_NAME,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.WHITE,
       VERSION,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.LIGHTBLACK_EX,
       Fore.GREEN,
       Fore.RESET)
    ]

ABOUT = ["""Domain Engineer or called as Domaineer is a tool to extract or dump any datas
of domains in hole net lines.
When you use this tool, It means you are accepting all of the
Terms and Conditions in Ethical Hacker's guide book. Hope you've read it.""",
         """This bot helps you in doing penetration testing, learning the ins and outs of domains,
analyzing objects, even doing stupid things like hacking your own domain and showing it off
in front of your friends.""",
         """A wide variety of hacking tools are here, use them with great care. Don't worry,
there is no backdoor logger here.
The bot will continue to be updated if bugs and changes are found to improve the quality of the bot
and update exploits"""
    ]

shuffle(BANNER)
shuffle(ABOUT)

# platform used
PLATFORM = os.name
PYVERSION = sys.version.split()[0]
IS_WIN = PLATFORM == "nt"

# Encoding used for Unicode data
UNICODE_ENCODING = "utf8"

# Maximum length of a help part containing switch/option name(s)
MAX_HELP_OPTION_LENGTH = 18

# Basic help options
BASIC_HELPS = [
    "url",
    "file_inp",
    "cli_based",
  ]
