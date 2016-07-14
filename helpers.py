from sys import exit
import spice

ANIME_QUERY_BASE  = 'http://myanimelist.net/api/anime/search.xml?q='
MANGA_QUERY_BASE  = 'http://myanimelist.net/api/manga/search.xml?q='

ANIME_SCRAPE_BASE = 'http://myanimelist.net/anime/'
MANGA_SCRAPE_BASE = 'http://myanimelist.net/manga/'

ANIME_UPDATE_BASE = 'http://myanimelist.net/api/animelist/update/id.xml'
ANIME_ADD_BASE    = 'http://myanimelist.net/api/animelist/add/id.xml'
ANIME_DELETE_BASE = 'http://myanimelist.net/api/animelist/delete/id.xml'

MANGA_UPDATE_BASE = 'http://myanimelist.net/api/mangalist/update/id.xml'
MANGA_ADD_BASE    = 'http://myanimelist.net/api/mangalist/add/id.xml'
MANGA_DELETE_BASE = 'http://myanimelist.net/api/mangalist/delete/id.xml'

ADD = "add"
UPDATE = "update"
DELETE = "delete"

def get_query_url(medium, query):
    query = query.strip()
    terms = query.replace(' ', '+')
    if medium == spice.ANIME:
        return ANIME_QUERY_BASE + terms
    elif medium == spice.MANGA:
        return MANGA_QUERY_BASE + terms
    else:
        return None

def get_scrape_url(id, medium):
    id_str = str(id).strip()
    if medium == spice.ANIME:
        return ANIME_SCRAPE_BASE + id_str
    elif medium == spice.MANGA:
        return MANGA_SCRAPE_BASE + id_str
    else:
        return None

def get_post_url(id, medium, op):
    if op == UPDATE:
        if medium == spice.ANIME:
            return ANIME_UPDATE_BASE.replace('id', str(id))
        elif medium == spice.MANGA:
            return MANGA_UPDATE_BASE.replace('id', str(id))
        else:
            return None
    elif op == ADD:
        if medium == spice.ANIME:
            return ANIME_ADD_BASE.replace('id', str(id))
        elif medium == spice.MANGA:
            return MANGA_ADD_BASE.replace('id', str(id))
        else:
            return None
    elif op == DELETE:
        if medium == spice.ANIME:
            return ANIME_DELETE_BASE.replace('id', str(id))
        elif medium == spice.MANGA:
            return MANGA_DELETE_BASE.replace('id', str(id))
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    exit(0)
