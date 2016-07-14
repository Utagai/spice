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

"""The credentials set for the user.
"""
this.credentials = None

class Medium:
    ANIME, MANGA = range(2)

def init_auth(username, password):
    """Initializes the auth settings for accessing MyAnimeList
    through its official API from a given username and password.
    :param username Your MyAnimeList account username.
    :param password Your MyAnimeList account password.
    :return A tuple containing your credentials.
    """
    this.credentials = (username, password)
    return (username, password)

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
        lines = [line for line in lines if len(line) != 0]
        if len(lines) == 2:
            this.credentials = (lines[0], lines[1])
            return (lines[0], lines[1])
        elif len(lines) == 1:
            user_pass = lines[0].split()
            this.credentials = (user_pass[0], user_pass[1])
            return (user_pass[0], user_pass[1])
        elif len(lines) == 0 or len(lines) > 2:
            return None

def search(query, medium):
    """Searches MyAnimeList for a [medium] matching the keyword(s) given by query.
    :param query  The keyword(s) to search with.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :return A list of all items that are of type [medium] and match the
             given keywords, or, an empty list if none matched.
    :raise ValueError For bad arguments.
    """
    if len(query) == 0:
        raise ValueError("Empty query.")
    api_query = helpers.get_query_url(medium, query)
    if api_query == None:
        raise ValueError("Invalid medium. Use spice.Medium.ANIME or spice.Medium.MANGA.")
    search_resp = requests.get(api_query, auth=credentials)
    if search_resp == None: #is there a better way to do this...
        return []
    results = BeautifulSoup(search_resp.text, 'lxml')
    if medium == Medium.ANIME:
        entries = results.anime
        if entries is None:
            sys.stderr.write("Too many requests... Waiting 5 seconds.\n")
            sleep(5)
            return search(query, medium)

        return [Anime(entry) for entry in entries.findAll('entry')]
    elif medium == Medium.MANGA:
        entries = results.manga
        if entries is None:
            sys.stderr.write("Too many requests.. Waiting 5 seconds.\n")
            sleep(5)
            return search(query, medium)
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
        raise ValueError("Id must be a non-zero, positive integer.")
    scrape_query = helpers.get_scrape_url(id, medium)
    if scrape_query == None:
        raise ValueError("Invalid medium. Use spice.Medium.ANIME or spice.Medium.MANGA.")
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
    """Adds the [medium] with the given id and data to the user's [medium]List.
    :param data   The data for the [medium] to add.
    :param id     The id of the data to add.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :raise ValueError For bad arguments.
    """
    _op(data, id, medium, helpers.Operations.ADD)

def update(data, id, medium):
    """Updates the [medium] with the given id and data on the user's [medium]List.
    :param data   The data for the [medium] to update.
    :param id     The id of the data to update.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :raise ValueError For bad arguments.
    """
    _op(data, id, medium, helpers.Operations.UPDATE)

def delete(data, id, medium):
    """Deletes the [medium] with the given id and data from the user's [medium]List.
    :param data   The data for the [medium] to delete.
    :param id     The id of the data to delete.
    :param medium Anime or manga (spice.Medium.Anime or spice.Medium.Manga).
    :raise ValueError For bad arguments.
    """
    _op(data, id, medium, helpers.Operations.DElETE)

def _op(data, id, medium, op):
    post = helpers.get_post_url(id, medium, op)
    if post is None:
        raise ValueError("Invalid medium. Use spice.Medium.ANIME or spice.Medium.MANGA.")
    post = post + ".xml?data=" + data.to_xml()
    headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}
    #MAL API is broken to hell -- you have to actually use GET
    #and chuck the data into the URL as seen above and below...
    r = requests.get(post, headers=headers, auth=credentials)

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

if __name__ == '__main__':
    print("Spice is meant to be imported into a project.")
