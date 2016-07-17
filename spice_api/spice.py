## A py module for the spice API.
##
## Oh, and a license thingy because otherwise it won't look cool and
## professional.
##
## MIT License
##
## Copyright (c) [2016] [Mehrab Hoque]
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the 'Software'), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

''' A py module for the spice API.

This module is meant to be imported into the project.

The spice API creates the idea of a 'Medium' which will be seen often in the
docs as [medium]. A [medium] is a concise way of describing either an anime or
a manga, as both are mediums through which the content is delivered.

The spice API exposes several functions for access to MAL:
0) init_auth()/load_auth_from_file() - Set and verify MAL credentials. Required.
1) search()                          - Search anime/manga by keyword.
2) search_id()                       - Grab anime/manga with a given id.
3) add()                             - Add an anime/manga to a list.
4) update()                          - Update an anime/manga on a list.
5) delete()                          - Delete an anime/manga from a list.
6) get_list()                        - Gets a user's Anime/MangaList.
7) get_blank()			             - Returns a blank Anime or MangaData object.
8) get_status()                      - Returns the status token for the given status string.
9) get_status_num()		     - Returns the status number for the given token or string.
10) get_medium() 		     - Returns the medium token for the given string.

The MediumList object returned by get_list() also exposes some useful functionality:
1) avg_score()         - Returns the user's average score across anime/manga watched.
2) median_score()      - Returns the user's median score across anime/manga watched.
3) mode_score()        - Returns the user's mode score across anime/manga watched.
4) p_stddev()          - Returns the pop. std. dev. of the user's score across anime/manga watched.
5) p_var()             - Returns the pop. variance of the user's score score across anime/manga watched.
6) score_diff()        - Returns the average score diff. of the user score across anime/manga watched.
		                 WARN: This is very slow and probably won't be implemented,
			             because of limitations of the MAL API.
7) get_num_status()    - Returns the number of anime/manga in [status] condition.
8) get_total()         - Returns the total number of anime/manga in the list across all statuses.
9) get_days()          - Returns the number of days spent watching/reading.
10) exists()           - Returns true or false if the given anime/manga exists in the list.
11) exists_as_status() - Returns true or false if the given anime/manga exists as the given status.
12) compatibility()    - Takes another MediumList and computes the compatibility according to the
			             algorithm specified by MAL.
13) get_scores()       - Returns a list of all scores in the list.
14) get_ids()          - Returns a list of all ids in the list.
15) get_titles()       - Returns a list of all titles in the list.
16) get_status()       - Returns a list of all items with the given status.
17) get_score()        - Returns a list of all items in the list with given score.
18) extremes()         - Returns a tuple containing the max and min score.

The spice API also exposes useful enums and values:
1) Medium enums    - ANIME|MANGA
2) Operation enums - ADD|UPDATE|DELETE
3) Status enums    - A translation for medium status numbers.
		             READING|1 & WATCHING|1
		             COMPLETED|2
                     ONHOLD|3
		             DROPPED|4
		             PLANTOREAD|6 & PLANTOWATCH|6
4) Key values      - Exposes an Anime/MangaList's sublist names, which are used
		             in he MediumList's implementation of its dictionary as keys.
		             READING     = 'reading'
		             WATCHING    = 'watching'
		             COMPLETED   = 'completed'
		             ONHOLD      = 'onhold'
		             DROPPED     = 'dropped'
		             PLANTOWATCH = 'plantowatch'
		             PLANTOREAD  = 'plantoread'


'''

from bs4 import BeautifulSoup
import requests
from . import objects
from . import constants
from . import helpers
from . import tokens
import sys

this = sys.modules[__name__]

'''The credentials set for the user.
'''
this.credentials = None

def init_auth(username, password):
    '''Initializes the auth settings for accessing MyAnimeList
    through its official API from a given username and password.
    :param username Your MyAnimeList account username.
    :param password Your MyAnimeList account password.
    :return A tuple containing your credentials.
    '''
    username = username.strip()
    password = password.strip()
    this.credentials = (username, password)
    if helpers.verif_auth(credentials):
        return (username, password)
    else:
        raise ValueError(constants.INVALID_CREDENTIALS)

def load_auth_from_file(filename):
    '''Initializes the auth settings for accessing MyAnimelist through its
    official API from a given filename.
    :param filename The name of the file containing your MyAnimeList
                    credentials
                    REQUIREMENTS: The file must...
                        ...username for your MAL account.
                        ...password for your MAL account.
                        ...Have both your username  and password
                        ...separated by newline(s) or space(s).
    :return A tuple containing your credentials.
    '''
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

        if helpers.verif_auth(credentials):
            return (lines[0], lines[1])
        else:
            raise ValueError(constants.INVALID_CREDENTIALS)

def search(query, medium):
    '''Searches MyAnimeList for a [medium] matching the keyword(s) given by query.
    :param query  The keyword(s) to search with.
    :param medium Anime or manga (tokens.Medium.ANIME or tokens.Medium.MANGA).
    :return A list of all items that are of type [medium] and match the
             given keywords, or, an empty list if none matched.
    :raise ValueError For bad arguments.
    '''
    if len(query) == 0:
        raise ValueError(constants.INVALID_EMPTY_QUERY)
    api_query = helpers.get_query_url(medium, query)
    if api_query is None:
        raise ValueError(constants.INVALID_MEDIUM)
    search_resp = requests.get(api_query, auth=credentials)
    if search_resp is None: #is there a better way to do this...
        return []
    query_soup = BeautifulSoup(search_resp.text, 'lxml')
    if medium == tokens.Medium.ANIME:
        entries = query_soup.anime
        if entries is None:
            return helpers.reschedule(search, constants.DEFAULT_WAIT, query, medium)

        return [objects.Anime(entry) for entry in entries.findAll('entry')]
    elif medium == tokens.Medium.MANGA:
        entries = query_soup.manga
        if entries is None:
            return helpers.reschedule(search, constants.DEFAULT_WAIT, query, medium)
        return [objects.Manga(entry) for entry in entries.findAll('entry')]

def search_id(id, medium):
    '''Grabs the [medium] with the given id from MyAnimeList as a [medium]
    object.
    :param id     The id of the [medium].
    :param medium Anime or manga (tokens.Medium.ANIME or tokens.Medium.MANGA).
    :return The [medium] object with id requested, or None if no such [medium]
            exists.
    :raise ValueError For bad arguments.
    '''
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
    '''Adds the [medium] with the given id and data to the user's [medium]List.
    :param data   The data for the [medium] to add.
    :param id     The id of the data to add.
    :param medium Anime or manga (tokens.Medium.ANIME or tokens.Medium.MANGA).
    :raise ValueError For bad arguments.
    '''
    _op(data, id, medium, tokens.Operations.ADD)

def update(data, id, medium):
    '''Updates the [medium] with the given id and data on the user's [medium]List.
    :param data   The data for the [medium] to update.
    :param id     The id of the data to update.
    :param medium Anime or manga (tokens.Medium.ANIME or tokens.Medium.MANGA).
    :raise ValueError For bad arguments.
    '''
    _op(data, id, medium, tokens.Operations.UPDATE)

def delete(data, id, medium):
    '''Deletes the [medium] with the given id and data from the user's [medium]List.
    :param data   The data for the [medium] to delete.
    :param id     The id of the data to delete.
    :param medium Anime or manga (tokens.Medium.ANIME or tokens.Medium.MANGA).
    :raise ValueError For bad arguments.
    '''
    _op(data, id, medium, tokens.Operations.DElETE)

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
        sys.stderr.write('This medium has not been approved by MAL yet.\n')
    elif constants.TOO_MANY_REQUESTS in op_resp.text: #Oh Holo save me from this API.
        helpers.reschedule(_op, constants.DEFAULT_WAIT, data, id, medium, op)

def get_blank(medium):
    '''Returns a [medium]Data object for filling before calling spice.add(),
    spice.update() or spice.delete().
    :param medium Anime or manga (tokens.Medium.ANIME or tokens.Medium.MANGA).
    :returns A [medium]Data object.
    '''
    if medium == tokens.Medium.ANIME:
        return objects.AnimeData()
    elif medium == tokens.Medium.MANGA:
        return objects.MangaData()
    else:
        return None

def get_list(medium, user=None):
    '''Returns a MediumList (Anime or Manga depends on [medium]) of user.
    If user is not given, the username is taken from the initialized auth
    credentials.
    :param medium Anime or manga (tokens.Medium.Anime or tokens.Medium.Manga)
    :param user   The user whose list should be grabbed. Defaults to credentials.
    '''
    if user is None:
        user = credentials[0]
    list_url = helpers.get_list_url(medium, user)
    list_resp = requests.get(list_url) #for some reason, we don't need auth.
    if constants.TOO_MANY_REQUESTS in list_resp.text:
        return helpers.reschedule(get_list, constants.DEFAULT_WAIT, medium, user)

    list_soup = BeautifulSoup(list_resp.text, 'lxml')
    return objects.MediumList(medium, list_soup)

def get_medium(medium):
    if medium == 'anime' or medium == 'ANIME' or medium == 'a' or medium == 'A':
        return tokens.Medium.ANIME
    elif medium == 'manga' or medium == 'MANGA' or medium == 'm' or medium == 'M':
        return tokens.Medium.MANGA
    else:
        raise ValueError(constants.INVALID_MEDIUM)

def get_status(status, s=True):
    if status in ['watching', 'WATCHING', 'w', 1, '1', 'watch']:
        return (tokens.Status.WATCHING if s else tokens.StatusNumber.WATCHING)
    elif status in ['reading', 'READING', 'r', 1, '1', 'read']:
        return tokens.Status.READING if s else tokens.StatusNumber.READING
    elif status in ['completed', 'COMPLETED', 'c', 2, '2', 'complete']:
        return tokens.Status.COMPLETED if s else tokens.StatusNumber.COMPLETED
    elif status in ['dropped', 'DROPPED', 'd', 3, '3', 'drop']:
        return tokens.Status.DROPPED if s else tokens.StatusNumber.DROPPED
    elif status in ['onhold', 'on-hold', 'ONHOLD', 'ON-HOLD', 'o', 4, '4']:
        return tokens.Status.ONHOLD if s else tokens.StatusNumber.ONHOLD
    elif status in ['plantowatch', 'PLANTOWATCH', 'plan-to-watch', 'p', 6, '6', 'pw']:
        return tokens.Status.PLANTOWATCH if s else tokens.StatusNumber.PLANTOWATCH
    elif status in ['plantoread', 'PLANTOREAD', 'plan-to-read', 'p', 6, '6', 'pr']:
        return tokens.Status.PLANTOREAD if s else tokens.StatusNumber.PLANTOREAD
    else:
        raise ValueError(constants.INVALID_STATUS)

def get_status_num(status):
    return get_status(status, False)

if __name__ == '__main__':
    print('Spice is meant to be imported into a project.')
