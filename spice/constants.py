## A py module for constants.
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

''' A py module for constants.

WARN: This module is not meant to be used in any way besides in the internals of
the spice API source code.
'''

'''The URL for verifying credentials.
'''
CREDENTIALS_VERIFY = 'http://myanimelist.net/api/account/verify_credentials.xml'

'''The base URLs for querying anime/manga searches based on keywords.
'''
ANIME_QUERY_BASE  = 'http://myanimelist.net/api/anime/search.xml?q='
MANGA_QUERY_BASE  = 'http://myanimelist.net/api/manga/search.xml?q='

'''The base URLs for scraping anime/manga based on id numbers.
'''
ANIME_SCRAPE_BASE = 'http://myanimelist.net/anime/'
MANGA_SCRAPE_BASE = 'http://myanimelist.net/manga/'

'''The base URLs for operations on a user's AnimeList.
'''
ANIME_ADD_BASE    = 'http://myanimelist.net/api/animelist/add/{}.xml'
ANIME_UPDATE_BASE = 'http://myanimelist.net/api/animelist/update/{}.xml'
ANIME_DELETE_BASE = 'http://myanimelist.net/api/animelist/delete/{}.xml'

'''The base URLs for operations on a user's MangaList.
'''
MANGA_UPDATE_BASE = 'http://myanimelist.net/api/mangalist/update/{}.xml'
MANGA_ADD_BASE    = 'http://myanimelist.net/api/mangalist/add/{}.xml'
MANGA_DELETE_BASE = 'http://myanimelist.net/api/mangalist/delete/{}.xml'

'''The base URLs for accessing a user's Anime or MangaList.
'''
ANIMELIST_BASE = 'http://myanimelist.net/malappinfo.php?u={}&status=all&type=anime'
MANGALIST_BASE = 'http://myanimelist.net/malappinfo.php?u={}&status=all&type=manga'

'''Global stats base URL, taken from MALGraph
'''
MALGRAPH_GLOBAL = 'http://graph.anime.plus/s/globals'

'''The default wait time before rescheduling an event.
'''
DEFAULT_WAIT = 5

'''Keyword substring for multiple requests --
The only way to consistently work around the inconsistency of the Official MAL
API.
'''
TOO_MANY_REQUESTS = 'Too Many Requests'

'''Arbitrary values that are unexplainable or confusing, that pop up in the code.
Hopefully, these constant names are more clear to the reader.
'''
UNAPPROVED = 'has not been approved'
OP_SUFFIX = '.xml?data='
ANIME_TITLE_ELEM = 'span'
ANIME_TITLE_ATTR = 'itemprop'
ANIME_TITLE_ATTR_VAL = 'name'

'''A collection of error message constants.
'''
INVALID_CREDENTIALS = 'Invalid credentials; rejected by MAL.'
INVALID_AUTH_FILE   = 'Invalid auth file.'
INVALID_EMPTY_QUERY = 'Must provide a non-empty query.'
INVALID_MEDIUM      = 'Invalid medium. Use spice.Medium.Anime or spice.Medium.MANGA.'
INVALID_ID          = 'Id must be a non-zero, positive integer.'
INVALID_STATUS_NUM  = 'Status num must be an integer (1, 2, 3, 4 or 6).'
INVALID_LIST_MATCH  = 'Invalid list match.'
