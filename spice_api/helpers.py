# A py module for helper functions.
#
# Oh, and a license thingy because otherwise it won't look cool and
# professional.
#
# MIT License
#
# Copyright (c) [2016] [Mehrab Hoque]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" A py module for helper functions.

WARN: This module is not meant to be used in any way besides in the internals 
of the tokens.API source code.
"""

from sys import exit
from time import sleep
from . import tokens
from . import constants
import requests


def get_query_url(medium, query):
    query = query.strip()
    terms = query.replace(' ', '+')
    if medium == tokens.Medium.ANIME:
        return constants.ANIME_QUERY_BASE + terms
    elif medium == tokens.Medium.MANGA:
        return constants.MANGA_QUERY_BASE + terms
    else:
        return None


def get_scrape_url(id, medium):
    id_str = str(id).strip()
    if medium == tokens.Medium.ANIME:
        return constants.ANIME_SCRAPE_BASE + id_str
    elif medium == tokens.Medium.MANGA:
        return constants.MANGA_SCRAPE_BASE + id_str
    else:
        return None


def get_post_url(id, medium, op):
    if op == tokens.Operations.ADD:
        if medium == tokens.Medium.ANIME:
            return constants.ANIME_ADD_BASE.format(id) +  constants.OP_SUFFIX
        elif medium == tokens.Medium.MANGA:
            return constants.MANGA_ADD_BASE.format(id) +  constants.OP_SUFFIX
    elif op == tokens.Operations.UPDATE:
        if medium == tokens.Medium.ANIME:
            return constants.ANIME_UPDATE_BASE.format(id) +  constants.OP_SUFFIX
        elif medium == tokens.Medium.MANGA:
            return constants.MANGA_UPDATE_BASE.format(id) +  constants.OP_SUFFIX
    else:
        if medium == tokens.Medium.ANIME:
            return constants.ANIME_DELETE_BASE.format(id) +  constants.OP_SUFFIX
        elif medium == tokens.Medium.MANGA:
            return constants.MANGA_DELETE_BASE.format(id) +  constants.OP_SUFFIX

    return None


def verif_auth(credentials, header):
    verif_resp = requests.get(constants.CREDENTIALS_VERIFY, auth=credentials,
                                headers=header)
    if constants.TOO_MANY_REQUESTS in verif_resp.text:
        return reschedule(verif_auth, constants.DEFAULT_WAIT, credentials)
    if verif_resp.status_code == 200:
        return True
    else:
        return False


def check_creds(credentials, header):
    if verif_auth(credentials, header):
        return True
    else:
        raise ValueError(constants.INVALID_CREDENTIALS)
        return False


def get_list_url(medium, user):
    if medium == tokens.Medium.ANIME:
        return constants.ANIMELIST_BASE.format(user)
    elif medium == tokens.Medium.MANGA:
        return constants.MANGALIST_BASE.format(user)
    else:
        return None


def reschedule(func, wait, *args):
    sleep(wait)
    return func(*args)


def find_key(status_num, medium):
    if status_num == str(tokens.StatusNumber.READING):
        if medium == tokens.Medium.MANGA:
            return tokens.Status.READING
        elif medium == tokens.Medium.ANIME:
            return tokens.Status.WATCHING
        else:
            raise ValueError(constants.INVALID_MEDIUM)
    elif status_num == str(tokens.StatusNumber.COMPLETED):
        return tokens.Status.COMPLETED
    elif status_num == str(tokens.StatusNumber.ONHOLD):
        return tokens.Status.ONHOLD
    elif status_num == str(tokens.StatusNumber.DROPPED):
        return tokens.Status.DROPPED
    elif status_num == str(tokens.StatusNumber.PLANTOREAD):
        if medium == tokens.Medium.MANGA:
            return tokens.Status.PLANTOREAD
        elif medium == tokens.Medium.ANIME:
            return tokens.Status.PLANTOWATCH
        else:
            raise ValueError(constants.INVALID_MEDIUM)
    else:
        raise ValueError(constants.INVALID_STATUS_NUM)


def find_key_num(status):
    if status == tokens.Status.WATCHING or status == tokens.Status.READING:
        return tokens.StatusNumber.WATCHING
    elif status == tokens.Status.COMPLETED:
        return tokens.StatusNumber.COMPLETED
    elif status == tokens.Status.DROPPED:
        return tokens.StatusNumber.DROPPED
    elif status == tokens.Status.ONHOLD:
        return tokens.StatusNumber.ONHOLD
    elif status == tokens.Status.PLANTOWATCH or status == tokens.Status.PLANTOREAD:
        return tokens.StatusNumber.PLANTOREAD
    else:
        return None


def det_key(status, medium):
    status = str(status)
    if status.isdigit(): # account for status num given
        status_key = find_key(status, medium)
    else:
        if status == tokens.Status.READING and medium == tokens.Medium.ANIME:
            status_key = tokens.Status.WATCHING
        elif status == tokens.Status.WATCHING and medium == tokens.Medium.MANGA:
            status_key = tokens.Status.READING
        elif status == tokens.Status.PLANTOREAD and medium == tokens.Medium.ANIME:
            status_key = tokens.Status.PLANTOWATCH
        elif status == tokens.Status.PLANTOWATCH and medium == tokens.Medium.MANGA:
            status_key = tokens.Status.PLANTOREAD
        else:
            status_key = status

    return status_key


if __name__ == '__main__':
    exit(0)
