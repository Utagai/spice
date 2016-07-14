from bs4 import BeautifulSoup
import requests
from objects import Anime
from objects import Manga
from objects import AnimeData
from objects import MangaData
import helpers
import sys
from time import sleep

this = sys.modules[__name__]
this.credentials = None

ANIME = 'anime'
MANGA = 'manga'

def init_auth(username, password):
    this.credentials = (username, password)
    return (username, password)

def search(query, medium):
    if len(query) == 0:
        return []
    api_query = helpers.get_query_url(medium, query)
    if api_query == None: #is there a better way to do this...
        return []
    search_resp = requests.get(api_query, auth=credentials)
    if search_resp == None: #is there a better way to do this...
        return []
    results = BeautifulSoup(search_resp.text, 'lxml')
    if medium == ANIME:
        entries = results.anime
        if entries is None:
            sys.stderr.write("Too many requests... Waiting 5 seconds.\n")
            sleep(5)
            return search(query, medium)

        return [Anime(entry) for entry in entries.findAll('entry')]
    elif medium == MANGA:
        entries = results.manga
        if entries is None:
            sys.stderr.write("Too many requests.. Waiting 5 seconds.\n")
            sleep(5)
            return search(query, medium)
        return [Manga(entry) for entry in entries.findAll('entry')]
    else:
        return []

def search_id(id, medium):
    if id <= 0:
        return None
    scrape_query = helpers.get_scrape_url(id, medium)
    if scrape_query == None:
        return None
    search_resp = requests.get(scrape_query)
    results = BeautifulSoup(search_resp.text, 'html.parser')
    #inspect element on an anime page, you'll see where this scrape is
    #coming from.
    query = results.find('span', {'itemprop':'name'})
    if query is None:
        print("Too many requests... Waiting 5 seconds.")
        sleep(5)
        return search_id(id, medium)
    matches = search(query.text, medium)
    index = [match.id for match in matches].index(str(id))
    if index != -1:
        return matches[index]
    else:
        return None

def add(data, id, medium):
    _op(data, id, medium, 'add')

def update(data, id, medium):
    _op(data, id, medium, 'update')

def delete(data, id, medium):
    _op(data, id, medium, 'delete')

def _op(data, id, medium, op):
    post = helpers.get_post_url(id, medium, op)
    post = post + ".xml?data=" + data.to_xml()
    headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}
    #MAL API is broken to hell -- you have to actually use GET
    #and chuck the data into the URL as seen above and below...
    r = requests.get(post, headers=headers, auth=credentials)

def get_blank(medium):
    if medium == ANIME:
        return AnimeData()
    elif medium == MANGA:
        return MangaData()
    else:
        return None

if __name__ == '__main__':
    print("Spice is meant to be imported into a project.")
