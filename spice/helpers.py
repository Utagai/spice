from sys import exit
from sys import stderr
from time import sleep
import spice

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
ANIME_ADD_BASE    = 'http://myanimelist.net/api/animelist/add/id.xml'
ANIME_UPDATE_BASE = 'http://myanimelist.net/api/animelist/update/id.xml'
ANIME_DELETE_BASE = 'http://myanimelist.net/api/animelist/delete/id.xml'

"""The base URLs for operations on a user's MangaList.
"""
MANGA_UPDATE_BASE = 'http://myanimelist.net/api/mangalist/update/id.xml'
MANGA_ADD_BASE    = 'http://myanimelist.net/api/mangalist/add/id.xml'
MANGA_DELETE_BASE = 'http://myanimelist.net/api/mangalist/delete/id.xml'

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
            return ANIME_ADD_BASE.replace('id', str(id))
        elif medium == spice.Medium.MANGA:
            return MANGA_ADD_BASE.replace('id', str(id))
        else:
            return None
    elif op == Operations.UPDATE:
        if medium == spice.Medium.ANIME:
            return ANIME_UPDATE_BASE.replace('id', str(id))
        elif medium == spice.Medium.MANGA:
            return MANGA_UPDATE_BASE.replace('id', str(id))
        else:
            return None
    else:
        if medium == spice.Medium.ANIME:
            return ANIME_DELETE_BASE.replace('id', str(id))
        elif medium == spice.Medium.MANGA:
            return MANGA_DELETE_BASE.replace('id', str(id))
        else:
            return None

def reschedule(func, *args):
    stderr.write("Too many requests. Waiting 5 seconds.\n")
    sleep(5)
    return func(*args)

if __name__ == '__main__':
    exit(0)
