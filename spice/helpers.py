from sys import exit
from sys import stderr
from time import sleep
import spice
import requests

"""The URL for verifying credentials.
"""
CREDENTIALS_VERIFY = 'http://myanimelist.net/api/account/verify_credentials.xml'

"""The base URLs for querying anime/manga searches based on keywords.
"""
ANIME_QUERY_BASE  = 'http://myanimelist.net/api/anime/search.xml?q='
MANGA_QUERY_BASE  = 'http://myanimelist.net/api/manga/search.xml?q='

"""The base URLs for scraping anime/manga based on id numbers.
"""
ANIME_SCRAPE_BASE = 'http://myanimelist.net/anime/'
MANGA_SCRAPE_BASE = 'http://myanimelist.net/manga/'

"""The base URLs for operations on a user's AnimeList.
"""
ANIME_ADD_BASE    = 'http://myanimelist.net/api/animelist/add/{}.xml'
ANIME_UPDATE_BASE = 'http://myanimelist.net/api/animelist/update/{}.xml'
ANIME_DELETE_BASE = 'http://myanimelist.net/api/animelist/delete/{}.xml'

"""The base URLs for operations on a user's MangaList.
"""
MANGA_UPDATE_BASE = 'http://myanimelist.net/api/mangalist/update/{}.xml'
MANGA_ADD_BASE    = 'http://myanimelist.net/api/mangalist/add/{}.xml'
MANGA_DELETE_BASE = 'http://myanimelist.net/api/mangalist/delete/{}.xml'

"""The base URLs for accessing a user's Anime or MangaList.
"""
ANIMELIST_BASE = 'http://myanimelist.net/malappinfo.php?u={}&status=all&type=anime'
MANGALIST_BASE = 'http://myanimelist.net/malappinfo.php?u={}&status=all&type=manga'

"""The operations available on user Lists."""
class Operations:
    ADD, UPDATE, DELETE = range(3)

def get_query_url(medium, query):
    query = query.strip()
    terms = query.replace(' ', '+')
    if medium == spice.Medium.ANIME:
        return ANIME_QUERY_BASE + terms
    elif medium == spice.Medium.MANGA:
        return MANGA_QUERY_BASE + terms
    else:
        return None

def get_scrape_url(id, medium):
    id_str = str(id).strip()
    if medium == spice.Medium.ANIME:
        return ANIME_SCRAPE_BASE + id_str
    elif medium == spice.Medium.MANGA:
        return MANGA_SCRAPE_BASE + id_str
    else:
        return None

def get_post_url(id, medium, op):
    if op == Operations.ADD:
        if medium == spice.Medium.ANIME:
            return ANIME_ADD_BASE.format(id)
        elif medium == spice.Medium.MANGA:
            return MANGA_ADD_BASE.format(id)
        else:
            return None
    elif op == Operations.UPDATE:
        if medium == spice.Medium.ANIME:
            return ANIME_UPDATE_BASE.format(id)
        elif medium == spice.Medium.MANGA:
            return MANGA_UPDATE_BASE.format(id)
        else:
            return None
    else:
        if medium == spice.Medium.ANIME:
            return ANIME_DELETE_BASE.format(id)
        elif medium == spice.Medium.MANGA:
            return MANGA_DELETE_BASE.format(id)
        else:
            return None

def verif_auth():
    verif_response = requests.get(CREDENTIALS_VERIFY, auth=spice.credentials)
    if verif_response.status_code == 200:
        return True
    else:
        return False


def get_list_url(medium):
    if medium == spice.Medium.ANIME:
        return ANIMELIST_BASE.format(spice.credentials[0])
    elif medium == spice.Medium.MANGA:
        return MANGALIST_BASE.format(spice.credentials[1])
    else:
        return None

def reschedule(func, *args):
    stderr.write("Too many requests. Waiting 5 seconds.\n")
    sleep(5)
    return func(*args)

if __name__ == '__main__':
    exit(0)
