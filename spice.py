from bs4 import BeautifulSoup
import requests
from objects import Anime
from objects import Manga
import sys

this = sys.modules[__name__]
this.credentials = None

ANIME_QUERY_BASE = 'http://myanimelist.net/api/anime/search.xml?q='
MANGA_QUERY_BASE = 'http://myanimelist.net/api/manga/search.xml?q='

ANIME_SCRAPE_BASE = 'http://myanimelist.net/anime/'
MANGA_SCRAPE_BASE = 'http://myanimelist.net/manga/'

ANIME = 'anime'
MANGA = 'manga'

def init_auth(username, password):
    this.credentials = (username, password)
    return (username, password)

def search(query, medium):
    query = query.strip()
    terms = query.replace(' ', '+')
    if medium == ANIME:
        api_query = ANIME_QUERY_BASE + terms
    else:
        api_query = MANGA_QUERY_BASE + terms
    search_resp = requests.get(api_query, auth=credentials)
    results = BeautifulSoup(search_resp.text, 'lxml')
    if medium == ANIME:
        return [Anime(entry) for entry in results.anime.findAll('entry')]
    else:
        return [Manga(entry) for entry in results.manga.findAll('entry')]

def search_id(id, medium):
    id_str = str(id).strip()
    if medium == ANIME:
        scrape_query = ANIME_SCRAPE_BASE + id_str
    else:
        scrape_query = MANGA_SCRAPE_BASE + id_str

    search_resp = requests.get(scrape_query)
    results = BeautifulSoup(search_resp.text, 'html.parser')
    #inspect element on an anime page, you'll see where this scrape is
    #coming from.
    query = results.find('span', {'itemprop':'name'})
    return search(query.text, medium)

def add(series):
    return

if __name__ == '__main__':
    print("Spice is meant to be imported into a project.")
