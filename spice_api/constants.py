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

# Default seconds to wait between requests
DEFAULT_WAIT_SECS = 3

# MyAnimeList URL Template declarations
BASE = 'https://myanimelist.net'
API_BASE = BASE + '/api'
ANIME_SCRAPE_BASE = BASE + '/anime/'
MANGA_SCRAPE_BASE = BASE + '/manga/'

CREDENTIALS_VERIFY = API_BASE + '/account/verify_credentials.xml'
ANIME_QUERY_BASE = API_BASE + '/anime/search.xml?q='
MANGA_QUERY_BASE = API_BASE + '/manga/search.xml?q='

ANIME_API_BASE = API_BASE + '/animelist'
ANIME_ADD_BASE = ANIME_API_BASE + '/add/{}.xml'
ANIME_DELETE_BASE = ANIME_API_BASE + '/delete/{}.xml'
ANIME_UPDATE_BASE = ANIME_API_BASE + '/update/{}.xml'

MANGA_API_BASE = API_BASE + '/mangalist'
MANGA_ADD_BASE = MANGA_API_BASE + '/add/{}.xml'
MANGA_DELETE_BASE = MANGA_API_BASE + '/delete/{}.xml'
MANGA_UPDATE_BASE = MANGA_API_BASE + '/update/{}.xml'

LIST_BASE = BASE + '/malappinfo.php?u={}&status=all&type='
ANIMELIST_BASE = LIST_BASE + 'anime'
MANGALIST_BASE = LIST_BASE + 'manga'

# Constants that have no other home
MALGRAPH_GLOBAL = 'http://graph.anime.plus/s/globals'
OP_SUFFIX = '.xml?data='

# Misc. error related globals
TOO_MANY_REQUESTS = 'Too Many Requests'
UNAPPROVED = 'has not been approved'

# Invalid related errors
INVALID_CREDENTIALS = 'Invalid credentials; rejected by MAL.'
INVALID_EMPTY_QUERY = 'Must provide a non-empty query.'
INVALID_LIST_MATCH = 'Invalid list match.'
INVALID_AUTH_FILE = 'Invalid auth file.'
INVALID_MEDIUM = 'Invalid medium. Use spice.Medium.Anime or spice.Medium.MANGA.'
INVALID_ID = 'Id must be a non-zero, positive integer.'
INVALID_STATUS = 'Status must be one of the following:' \
                 '\nReading(1)' \
                 '\nWatching(1)' \
                 '\nCompleted(2)' \
                 '\nOnhold(3)' \
                 '\nDropped(4)' \
                 '\nPlanToRead(6)' \
                 '\nPlanToWatch(6)'
INVALID_STATUS_NUM = INVALID_STATUS
