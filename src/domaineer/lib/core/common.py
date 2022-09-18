#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

from re import findall
from colorama import Fore

from lib.core.exception import (
    UserFailedInput,
    DateFormatError,
    DateLenghtError
    )
from lib.core.settings import BANNER, ABOUT

def banner():
    writeLn("", BANNER + ABOUT)

def Switch(list_opt: dict, option: str):
    try:
        if option not in list_opt:
            raise UserFailedInput
        opt_val = list_opt[option]
        return opt_val

    except UserFailedInput:
        return False

def writeLn(param : str, text_out: str):
    if param == "":
        print(text_out)
    else:
        p_txt,c_txt = Switch({
            "i" : ('INFO', Fore.GREEN),
            "w" : ('WARN', Fore.YELLOW),
            "e" : ('ERROR', Fore.RED)
        }, param)
        print("\r[ %s%s%s ] %s•%s %s" %
              (c_txt,p_txt,Fore.RESET,c_txt,Fore.RESET,text_out)
              )

def readLn(text: str):
    text_put = input("[ %sQUEST%s ] %s•%s %s " % (Fore.BLUE,Fore.RESET,Fore.BLUE,Fore.RESET,text))
    return text_put

def list_to_date(listin : list) -> str:
    month_str = {
        "01":"Jan",
        "02":"Feb",
        "03":"Mar",
        "04":"Apr",
        "05":"May",
        "06":"Jun",
        "07":"Jul",
        "08":"Aug",
        "09":"Sep",
        "10":"Oct",
        "11":"Nov",
        "12":"Dec"
    }
    month_num = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    if listin[1] in month_num:
        month = listin[1].replace(listin[1],month_str[listin[1]])
    else:
        month = listin[1]

    return "".join(listin[0]+" "+month+" "+listin[2])

def monthstrtoint(string) -> str:
    chrs = {
        "Jan":"01",
        "Feb":"02",
        "Mar":"03",
        "Apr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Aug":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12"
    }
    try:
        return chrs[string]
    except:
        return string

def input_date(date_str: str) -> list:
    if " " in date_str:
        date = date_str.split(" ")
    elif "," in date_str:
        date = date_str.split(",")
    elif "-" in date_str:
        date = date_str.split("-")
    elif "/" in date_str:
        date = date_str.split("/")
    else:
        pass
    if len(date) != 3:
        errMsg = "Date Lenght Should be 3"
        raise DateFormatError(errMsg)
    if len(date[0]) != 2:
        raise DateLenghtError
    if len(date[1]) > 3:
        raise DateLenghtError
    if len(date[2]) != 4:
        raise DateLenghtError
    if findall(r"(0).",date[0]):
        date[0] = date[0].replace("0","")
    if findall(r"(0).",date[1]):
        date[1] = date[1].replace("0","")

    return date
