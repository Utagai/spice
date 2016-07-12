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

ANIME_UPDATE_BASE = 'http://myanimelist.net/api/animelist/update/id.xml'

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
    matches = search(query.text, medium)
    for match in matches:
        if match.id == str(id):
            return match

    return None

def update(data, id):
    print(data.to_xml())
    series_data = {'data':data.to_xml()}
    post = ANIME_UPDATE_BASE.replace('id', str(id))
    headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}
    r = requests.post(post, data=series_data, headers=headers, auth=credentials)
    print(r.text)

if __name__ == '__main__':
    print("Spice is meant to be imported into a project.")
