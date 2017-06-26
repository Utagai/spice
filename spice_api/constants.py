"""MIT License

Copyright (c) [2016] [Mehrab Hoque]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


A py module for constants.
"""

CREDENTIALS_VERIFY = ('https://myanimelist.net/api/account/' + 
                      'verify_credentials.xml')
""" The URL for verifying credentials.
"""

ANIME_QUERY_BASE = 'https://myanimelist.net/api/anime/search.xml?q='
"""The base URLs for querying anime searches based on keywords.
"""
MANGA_QUERY_BASE = 'https://myanimelist.net/api/manga/search.xml?q='
"""The base URLs for querying manga searches based on keywords.
"""

ANIME_SCRAPE_BASE = 'https://myanimelist.net/anime/'
"""The base URLs for scraping anime based on id numbers.
"""
MANGA_SCRAPE_BASE = 'https://myanimelist.net/manga/'
"""The base URLs for scraping manga based on id numbers.
"""

ANIME_ADD_BASE = 'https://myanimelist.net/api/animelist/add/{}.xml'
"""The base URL for an add operation on a user's AnimeList.
"""
ANIME_UPDATE_BASE = 'https://myanimelist.net/api/animelist/update/{}.xml'
"""The base URL for an update operation on a user's AnimeList.
"""
ANIME_DELETE_BASE = 'https://myanimelist.net/api/animelist/delete/{}.xml'
"""The base URL for a delete operation on a user's AnimeList.
"""

MANGA_UPDATE_BASE = 'https://myanimelist.net/api/mangalist/update/{}.xml'
"""The base URL for an add operation on a user's MangaList.
"""
MANGA_ADD_BASE = 'https://myanimelist.net/api/mangalist/add/{}.xml'
"""The base URL for an update operation on a user's MangaList.
"""
MANGA_DELETE_BASE = 'https://myanimelist.net/api/mangalist/delete/{}.xml'
"""The base URL for a delete operation on a user's MangaList.
"""

ANIMELIST_BASE = ('https://myanimelist.net/malappinfo.php?u={}&' + 
                  'status=all&type=anime')
"""The base URLs for accessing a user's AnimeList.
"""
MANGALIST_BASE = ('https://myanimelist.net/malappinfo.php?u={}&' +
                  'status=all&type=manga')
"""The base URLs for accessing a user's MangaList.
"""

MALGRAPH_GLOBAL = 'http://graph.anime.plus/s/globals'
"""Global stats base URL, taken from MALGraph
"""

DEFAULT_WAIT = 3
"""The default wait time before rescheduling an event.
"""

TOO_MANY_REQUESTS = 'Too Many Requests'
"""Keyword substring for multiple requests --
The only way to consistently work around the inconsistency of the Official MAL
API.
"""

UNAPPROVED = 'has not been approved'
OP_SUFFIX = '.xml?data='
ANIME_TITLE_ELEM = 'span'
ANIME_TITLE_ATTR = 'itemprop'
ANIME_TITLE_ATTR_VAL = 'name'
"""Arbitrary values that are unexplainable or confusing, that pop up in the 
code. Hopefully, these constant names are more clear to the reader.
"""

INVALID_CREDENTIALS = 'Invalid credentials; rejected by MAL.'
INVALID_AUTH_FILE = 'Invalid auth file.'
INVALID_EMPTY_QUERY = 'Must provide a non-empty query.'
INVALID_MEDIUM = 'Invalid medium. Use spice.get_medium().'
INVALID_ID = 'Id must be a non-zero, positive integer.'
INVALID_STATUS = '''Status must be one of the following:
\'reading(1)\'\n\'watching(1)\'\n\'completed(2)\'
\'onhold(3)\'\n\'dropped(4)\'\n\'plantoread(6)\'
\'plantowatch(6)\''''
INVALID_STATUS_NUM = '''Status must be one of the following:
\'reading(1)\'\n\'watching(1)\'\n\'completed(2)\'
\'onhold(3)\'\n\'dropped(4)\'\n\'plantoread(6)\'
\'plantowatch(6)\''''
INVALID_LIST_MATCH = 'Invalid list match.'
