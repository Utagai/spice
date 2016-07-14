from sys import exit
from sys import stderr
from time import sleep
import spice
import constants
import requests

def get_query_url(medium, query):
    query = query.strip()
    terms = query.replace(' ', '+')
    if medium == spice.Medium.ANIME:
        return constants.ANIME_QUERY_BASE + terms
    elif medium == spice.Medium.MANGA:
        return constants.MANGA_QUERY_BASE + terms
    else:
        return None

def get_scrape_url(id, medium):
    id_str = str(id).strip()
    if medium == spice.Medium.ANIME:
        return constants.ANIME_SCRAPE_BASE + id_str
    elif medium == spice.Medium.MANGA:
        return constants.MANGA_SCRAPE_BASE + id_str
    else:
        return None

def get_post_url(id, medium, op):
    if op == spice.Operations.ADD:
        if medium == spice.Medium.ANIME:
            return constants.ANIME_ADD_BASE.format(id)
        elif medium == spice.Medium.MANGA:
            return constants.MANGA_ADD_BASE.format(id)
        else:
            return None
    elif op == spice.Operations.UPDATE:
        if medium == spice.Medium.ANIME:
            return constants.ANIME_UPDATE_BASE.format(id)
        elif medium == spice.Medium.MANGA:
            return constants.MANGA_UPDATE_BASE.format(id)
        else:
            return None
    else:
        if medium == spice.Medium.ANIME:
            return constants.ANIME_DELETE_BASE.format(id)
        elif medium == spice.Medium.MANGA:
            return constants.MANGA_DELETE_BASE.format(id)
        else:
            return None

def verif_auth():
    verif_resp = requests.get(constants.CREDENTIALS_VERIFY,
                              auth=spice.credentials)
    if verif_resp.status_code == 200:
        return True
    else:
        return False


def get_list_url(medium):
    if medium == spice.Medium.ANIME:
        return constants.ANIMELIST_BASE.format(spice.credentials[0])
    elif medium == spice.Medium.MANGA:
        return constants.MANGALIST_BASE.format(spice.credentials[1])
    else:
        return None

def reschedule(func, wait, *args):
    stderr.write("Too many requests. Waiting 5 seconds.\n")
    sleep(wait)
    return func(*args)

if __name__ == '__main__':
    exit(0)
