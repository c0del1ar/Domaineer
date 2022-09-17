#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

try:
    from optparse import OptionParser as ArgumentParser
    from optparse import OptioneError as ArgumentError
    from optparse import OptionGroup
    from optparse import SUPPRESS_HELP as SUPPRESS

    def _add_argument_group(self, *args, **kwargs):
        return self.add_option_group(OptionGroup(self, *args, **kwargs))

    ArgumentParser.add_argument_group = _add_argument_group

    def _add_argument(self, *args, **kwargs):
        return self.add_option(*args, **kwargs)

    OptionGroup._add_argument = _add_argument
    ArgumentParser.add_argument = ArgumentParser.add_option

except ImportError:
    from argparse import (
        ArgumentParser,
        ArgumentError,
        SUPPRESS
    )

finally:
    def get_actions(instance):
        for attr in ("option_list", "_group_actions", "_actions"):
            if hasattr(instance, attr):
                return getattr(instance, attr)

    def get_groups(parser):
        return getattr(parser, "option_groups", None) or getattr(parser, "_action_groups")

    def get_all_options(parser):
        retVal = set()

        for option in get_actions(parser):
            if hasattr(option, "option_strings"):
                retVal.update(option.option_strings)
            else:
                retVal.update(option._long_opts)
                retVal.update(option._short_opts)

        for group in get_groups(parser):
            for option in get_actions(group):
                if hasattr(option, "option_strings"):
                    retVal.update(option.option_strings)
                else:
                    retVal.update(option._long_opts)
                    retVal.update(option._short_opts)

        return retVal

import os
import sys
import re

from lib.core.common import writeLn
from lib.core.settings import (
    BANNER,
    ABOUT,
    VERSION,
    IS_WIN,
    MAX_HELP_OPTION_LENGTH,
    BASIC_HELPS)

def ArgParser(argv=None):
    if not argv:
        argv = sys.argv
    _ = os.path.basename(argv[0])

    desc = "%s\n%s" % (BANNER[0], ABOUT[0])
    usage = "%s%s [options]" % (
        "%s " % os.path.basename(sys.executable)
        if not IS_WIN else "",
        "\"%s\"" % _ if " " in _ else _
    )
    parser = ArgumentParser(usage=usage)

    try:
        parser.add_argument("--hh", dest="advancedHelp",action="store_true",
                            help="Show advanced help and exit")
        parser.add_argument("--version", dest="showVersion", action="store_true",
                            help="Show program's version number and exit")

        # App based
        based = parser.add_argument_group("App Based", "You must specify the app run with")
        based.add_argument("--cli", dest="cli_based", action="store_true",
            help="App will run in CLI mode")

        # Tool Choice
        tool = parser.add_argument_group("Tool/Exploit", "Tool we provide for make you easier to hack")
        tool.add_argument("--grabber", dest="grabber", action="store_true",
                          help="Domains grabbing")
        tool.add_argument("--rev-ip", dest="reverser_ip", action="store_true",
                          help="Reverse IP")
        tool.add_argument("--cms-scan", dest="cms_scan", action="store_true",
                          help="Content Management System scan")
        tool.add_argument("--fuzz", dest="fuzz", action="store_true",
                          help="Web fuzzer")
        tool.add_argument("--search", dest="search_engine", action="store_true",
                          help="Search engine")
        tool.add_argument("--domainip", dest="Domain", action="store_true",
                          help="Domain to ip converter")

        # Common command
        parser.add_argument("-u", "--url", dest="url",
                            help="Target URL")
        parser.add_argument("-f", "--file", dest="file_inp", metavar="FILE",
                            help="File input")

        # Dirty hack to display longer options without breaking into two lines
        if hasattr(parser, "formatter"):
            def _(self, *args):
                retVal = parser.formatter._format_option_strings(*args)
                if len(retVal) > MAX_HELP_OPTION_LENGTH:
                    retVal = ("%%.%ds.." % (MAX_HELP_OPTION_LENGTH - parser.formatter.indent_increment)) % retVal
                return retVal

            parser.formatter._format_option_strings = parser.formatter.format_option_strings
            parser.formatter.format_option_strings = type(parser.formatter.format_option_strings)(_, parser)
        else:
            def _format_action_invocation(self, action):
                retVal = self.__format_action_invocation(action)
                if len(retVal) > MAX_HELP_OPTION_LENGTH:
                    retVal = ("%%.%ds.." % (MAX_HELP_OPTION_LENGTH - self._indent_increment)) % retVal
                return retVal

            parser.formatter_class.__format_action_invocation = parser.formatter_class._format_action_invocation
            parser.formatter_class._format_action_invocation = _format_action_invocation

        # Dirty hack for making a short option '-hh'
        if hasattr(parser, "get_option"):
            option = parser.get_option("--hh")
            option._short_opts = ["-hh"]
            option._long_opts = []
        else:
            for action in get_actions(parser):
                if action.option_strings == ["--hh"]:
                    action.option_strings = ["-hh"]
                    break

        # Dirty hack for inherent help message of switch '-h'
        if hasattr(parser, "get_option"):
            option = parser.get_option("-h")
            option.help = option.help.capitalize().replace("this help", "basic help")
        else:
            for action in get_actions(parser):
                if action.option_strings == ["-h", "--help"]:
                    action.help = action.help.capitalize().replace("this help", "basic help")
                    break

        _ = []
        advancedHelp = True

        for arg in argv:
            _.append(arg)

        argv = _

        #longOptions = set(re.findall(r"\-\-([^= ]+?)=", parser.format_help()))
        #longSwitches = set(re.findall(r"\-\-([^= ]+?)\s", parser.format_help()))

        for i in range(len(argv)):
            if argv[i] in ("-h", "--help"):
                advancedHelp = False
                for group in get_groups(parser)[:]:
                    found = False
                    for option in get_actions(group):
                        if option.dest not in BASIC_HELPS:
                            option.help = SUPPRESS
                        else:
                            found = True
                    if not found:
                        get_groups(parser).remove(group)
            elif argv[i] == "--version":
                writeLn("i", VERSION)
                raise SystemExit

        if len(argv) == 1:
            print(desc)
            parser.print_usage()
            raise SystemExit

        try:
            (args, _) = (parser.parse_known_args(argv)
                         if hasattr(parser, "parse_known_args")
                         else parser.parse_args(argv)
                         )
        except UnicodeEncodeError as ex:
            writeLn("e", ex.object.encode("unicode-escape"))
            raise SystemExit
        except SystemExit:
            if "-h" in argv and not advancedHelp:
                writeLn("i", "To see full list of options run with '-hh'\n")
            raise

        return args
    except (ArgumentError, TypeError) as ex:
        parser.error(ex)
