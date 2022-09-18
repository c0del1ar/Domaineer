#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

from colorama import init, Fore
from prettytable.colortable import ColorTable, Theme

from lib.core.settings import TOOL_LIST, TOOL_COUNT

init()

class Themes:
    DEFAULT = Theme()
    OCEAN = Theme(
        default_color="96",
        vertical_color="34",
        horizontal_color="34",
        junction_color="36",
    )
    HACKER = Theme(
        default_color="40",
        vertical_color="32",
        horizontal_color="92",
        junction_color="92"
    )

def tabulation(table_set : str):
    if table_set == "tool":
        table = ColorTable(theme=Themes.HACKER)
        table.field_names = ["No", "Name", "Args", "Status"]
        for x in range(TOOL_COUNT):
            tl = TOOL_LIST
            _args = ("--" + tl["argument"][x]
                     if tl["argument"][x] != ""
                     else "-")
            _status = (Fore.LIGHTGREEN_EX + "ON" + Fore.RESET
                       if tl["status"][x] == 1
                       else Fore.LIGHTRED_EX + "OFF" + Fore.RESET
                       )
            table.add_row([
                x+1,tl["name"][x],_args,_status
            ])
    else:
        table = ColorTable(theme=Themes.DEFAULT)

    return table
