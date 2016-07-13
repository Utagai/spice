from sys import exit
import spice

def get_query_url(id, medium, query):
    query = query.strip()
    terms = query.replace(' ', '+')
    if medium == spice.ANIME:
        return spice.ANIME_QUERY_BASE + terms
    elif medium == spice.MANGA:
        return spice.MANGA_QUERY_BASE + terms
    else:
        return None

def get_scrape_url(id, medium):
    id_str = str(id).strip()
    if medium == spice.ANIME:
        return spice.ANIME_SCRAPE_BASE + id_str
    elif medium == spice.MANGA:
        return spice.MANGA_SCRAPE_BASE + id_str
    else:
        return None

def get_post_url(id, medium, op):
    if op == spice._UPDATE:
        if medium == spice.ANIME:
            return spice.ANIME_UPDATE_BASE.replace('id', str(id))
        elif medium == spice.MANGA:
            return spice.MANGA_UPDATE_BASE.replace('id', str(id))
        else:
            return None
    elif op == spice._ADD:
        if medium == spice.ANIME:
            return spice.ANIME_ADD_BASE.replace('id', str(id))
        elif medium == spice.MANGA:
            return spice.MANGA_ADD_BASE.replace('id', str(id))
        else:
            return None
    elif op == spice._DELETE:
        if medium == spice.ANIME:
            return spice.ANIME_DELETE_BASE.replace('id', str(id))
        elif medium == spice.MANGA:
            return spice.MANGA_DELETE_BASE.replace('id', str(id))
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    exit(0)
