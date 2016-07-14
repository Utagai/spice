"""The URL for verifying credentials.
"""
CREDENTIALS_VERIFY = 'http://myanimelist.net/api/account/verify_credentials.xml'

"""The base URLs for querying anime/manga searches based on keywords.
"""
ANIME_QUERY_BASE  = 'http://myanimelist.net/api/anime/search.xml?q='
MANGA_QUERY_BASE  = 'http://myanimelist.net/api/manga/search.xml?q='

"""The base URLs for scraping anime/manga based on id numbers.
"""
ANIME_SCRAPE_BASE = 'http://myanimelist.net/anime/'
MANGA_SCRAPE_BASE = 'http://myanimelist.net/manga/'

"""The base URLs for operations on a user's AnimeList.
"""
ANIME_ADD_BASE    = 'http://myanimelist.net/api/animelist/add/{}.xml'
ANIME_UPDATE_BASE = 'http://myanimelist.net/api/animelist/update/{}.xml'
ANIME_DELETE_BASE = 'http://myanimelist.net/api/animelist/delete/{}.xml'

"""The base URLs for operations on a user's MangaList.
"""
MANGA_UPDATE_BASE = 'http://myanimelist.net/api/mangalist/update/{}.xml'
MANGA_ADD_BASE    = 'http://myanimelist.net/api/mangalist/add/{}.xml'
MANGA_DELETE_BASE = 'http://myanimelist.net/api/mangalist/delete/{}.xml'

"""The base URLs for accessing a user's Anime or MangaList.
"""
ANIMELIST_BASE = 'http://myanimelist.net/malappinfo.php?u={}&status=all&type=anime'
MANGALIST_BASE = 'http://myanimelist.net/malappinfo.php?u={}&status=all&type=manga'

