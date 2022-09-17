#!/usr/bin/env python

"""
Copyright (c) 2021 Domaineer
Semi-Auto Exploitation tool by Arya Kresna
https://github.com/c0del1ar/Domaineer
"""

class AppError(Exception):
    pass

class UserFailedInput(AppError):
    pass

class UserCancelled(AppError):
    pass

class ServerConnectFailed(AppError):
    pass

class DateFormatError(AppError):
    pass

class DateLenghtError(AppError):
    pass

class MaxPageExceed(AppError):
    pass
