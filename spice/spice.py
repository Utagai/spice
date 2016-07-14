from bs4 import BeautifulSoup
import requests
from objects import Anime
from objects import Manga
from objects import AnimeData
from objects import MangaData
from objects import MediumList
import constants
import helpers
import sys

this = sys.modules[__name__]

"""The credentials set for the user.
"""
this.credentials = None

"""The class that defines 'mediums'. Commonly seen as [medium] through the
docs. A medium is the form in which the content comes in, and can either be
ANIME or MANGA.

These are to be treated like enum tokens and are used frequently in this API's
function calls to specify the medium for which to do work, since MyAnimeList
is very distinctly cut up into two pieces, one for anime and one for manga.
"""
class Medium:
    ANIME, MANGA = range(2)

"""The operations available on user Lists. These are to be treated like enums
."""
class Operations:
    ADD, UPDATE, DELETE = range(3)

"""The numerical translations for anime/manga statuses. These are to be treated
like enums.
"""
class Status:
    READING = 1
    WATCHING, COMPLETED, ONHOLD, DROPPED = range(1,5)
    PLANTOWATCH = 6
    PLANTOREAD = 6

"""A namespace for exposing key names in AnimeList and MangaList object
dictionaries.
"""
class Keys:
    READING = 'reading'
    WATCHING = 'watching'
    COMPLETED = 'completed'
    ONHOLD = 'onhold'
    DROPPED = 'dropped'
    PLANTOWATCH = 'plantowatch'
    PLANTOREAD = 'plantoread'

def init_auth(username, password):
    """Initializes the auth settings for accessing MyAnimeList
    through its official API from a given username and password.
    :param username Your MyAnimeList account username.
    :param password Your MyAnimeList account password.
    :return A tuple containing your credentials.
    """
    username = username.strip()
    password = password.strip()
    this.credentials = (username, password)
    if helpers.verif_auth():
        return (username, password)
    else:
        raise ValueError(constants.INVALID_CREDENTIALS)

def load_auth_from_file(filename):
    """Initializes the auth settings for accessing MyAnimelist through its
    official API from a given filename.
    :param filename The name of the file containing your MyAnimeList
                    credentials
                    REQUIREMENTS: The file must...
                        ...username for your MAL account.
                        ...password for your MAL account.
                        ...Have both your username  and password
                        ...separated by newline(s) or space(s).
    :return A tuple containing your credentials.
    """
    with open(filename) as auth_file:
        lines = auth_file.read().splitlines()
        lines = [line.strip() for line in lines if len(line) != 0]
        if len(lines) == 2:
            this.credentials = (lines[0], lines[1])
        elif len(lines) == 1:
            user_pass = lines[0].split()
            this.credentials = (user_pass[0], user_pass[1])
        elif len(lines) == 0 or len(lines) > 2:
            raise ValueError(constants.INVALID_AUTH_FILE)

        if helpers.verif_auth():
            return (lines[0], lines[1])
        else:
            raise ValueError(constants.INVALID_CREDENTIALS)

def search(query, medium):
    """Searches MyAnimeList for a [medium] matching the keyword(s) given by query.
    :param query  The keyword(s) to search with.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :return A list of all items that are of type [medium] and match the
             given keywords, or, an empty list if none matched.
    :raise ValueError For bad arguments.
    """
    if len(query) == 0:
        raise ValueError(constants.INVALID_EMPTY_QUERY)
    api_query = helpers.get_query_url(medium, query)
    if api_query is None:
        raise ValueError(constants.INVALID_MEDIUM)
    search_resp = requests.get(api_query, auth=credentials)
    if search_resp is None: #is there a better way to do this...
        return []
    query_soup = BeautifulSoup(search_resp.text, 'lxml')
    if medium == Medium.ANIME:
        entries = query_soup.anime
        if entries is None:
            return helpers.reschedule(search, constants.DEFAULT_WAIT, query, medium)

        return [Anime(entry) for entry in entries.findAll('entry')]
    elif medium == Medium.MANGA:
        entries = query_soup.manga
        if entries is None:
            return helpers.reschedule(search, constants.DEFAULT_WAIT, query, medium)
        return [Manga(entry) for entry in entries.findAll('entry')]

def search_id(id, medium):
    """Grabs the [medium] with the given id from MyAnimeList as a [medium]
    object.
    :param id     The id of the [medium].
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :return The [medium] object with id requested, or None if no such [medium]
            exists.
    :raise ValueError For bad arguments.
    """
    if id <= 0 or not float(id).is_integer():
        raise ValueError(constants.INVALID_ID)
    scrape_query = helpers.get_scrape_url(id, medium)
    if scrape_query is None:
        raise ValueError(constants.INVALID_MEDIUM)
    search_resp = requests.get(scrape_query)
    scrape_soup = BeautifulSoup(search_resp.text, 'html.parser')
    #inspect element on an anime page, you'll see where this scrape is
    #coming from.
    query = scrape_soup.find(constants.ANIME_TITLE_ELEM,
                    {constants.ANIME_TITLE_ATTR:constants.ANIME_TITLE_ATTR_VAL})
    if query is None:
        return helpers.reschedule(search_id, constants.DEFAULT_WAIT, id, medium)
    matches = search(query.text, medium)
    index = [match.id for match in matches].index(str(id))
    if index != -1:
        return matches[index]
    else:
        return None

def add(data, id, medium):
    """Adds the [medium] with the given id and data to the user's [medium]List.
    :param data   The data for the [medium] to add.
    :param id     The id of the data to add.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :raise ValueError For bad arguments.
    """
    _op(data, id, medium, Operations.ADD)

def update(data, id, medium):
    """Updates the [medium] with the given id and data on the user's [medium]List.
    :param data   The data for the [medium] to update.
    :param id     The id of the data to update.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :raise ValueError For bad arguments.
    """
    _op(data, id, medium, Operations.UPDATE)

def delete(data, id, medium):
    """Deletes the [medium] with the given id and data from the user's [medium]List.
    :param data   The data for the [medium] to delete.
    :param id     The id of the data to delete.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :raise ValueError For bad arguments.
    """
    _op(data, id, medium, Operations.DElETE)

def _op(data, id, medium, op):
    post = helpers.get_post_url(id, medium, op)
    if post is None:
        raise ValueError(constants.INVALID_MEDIUM)
    post = post  + data.to_xml()
    headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}
    #MAL API is broken to hell -- you have to actually use GET
    #and chuck the data into the URL as seen above and below...
    op_resp = requests.get(post, headers=headers, auth=credentials)
    if op_resp.status_code == 400 and constants.UNAPPROVED in op_resp.text:
        sys.stderr.write("This medium has not been approved by MAL yet.\n")
    elif constants.TOO_MANY_REQUESTS in op_resp.text: #Oh Holo save me from this API.
        helpers.reschedule(_op, constants.DEFAULT_WAIT, data, id, medium, op)

def get_blank(medium):
    """Returns a [medium]Data object for filling before calling spice.add(),
    spice.update() or spice.delete().
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :returns A [medium]Data object.
    """
    if medium == Medium.ANIME:
        return AnimeData()
    elif medium == Medium.MANGA:
        return MangaData()
    else:
        return None

def get_list(medium, user=None):
    if user is None:
        user = credentials[0]
    print(user)
    list_url = helpers.get_list_url(medium, user)
    list_resp = requests.get(list_url) #for some reason, we don't need auth.
    if constants.TOO_MANY_REQUESTS in list_resp.text:
        helpers.reschedule(get_list, constants.DEFAULT_WAIT, medium)

    return MediumList(medium, list_resp.text)

if __name__ == '__main__':
    print("Spice is meant to be imported into a project.")
