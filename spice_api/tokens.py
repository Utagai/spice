# A py module for token values.
#
# Oh, and a license thingy because otherwise it won't look cool and
# professional.
#
# MIT License
#
# Copyright (c) [2016] [Mehrab Hoque]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""" A py module for token values.

[medium]
[keys]
[operations]
[status]
[statusnumber]

WARN: This module is not meant to be used in any way besides in the internals of
the spice API source code.
"""

"""The class that defines 'mediums'. Commonly seen as [medium] through the
docs. A medium is the form in which the content comes in, and can either be
ANIME or MANGA.

These are to be treated like enum tokens and are used frequently in this API's
function calls to specify the medium for which to do work, since MyAnimeList
is very distinctly cut up into two pieces, one for anime and one for manga.
"""
class Medium:
    ANIME, MANGA = list(range(2))

"""The operations available on user Lists. These are to be treated like enums
."""
class Operations:
    ADD, UPDATE, DELETE = list(range(3))

"""The numerical translations for anime/manga statuses. These are to be treated
like enums.
"""
class StatusNumber:
    READING     = 1
    WATCHING, COMPLETED, ONHOLD, DROPPED = list(range(1,5))
    PLANTOWATCH = 6
    PLANTOREAD  = 6

"""A namespace for exposing key names in AnimeList and MangaList object
dictionaries.
"""
class Status:
    READING     = 'reading'
    WATCHING    = 'watching'
    COMPLETED   = 'completed'
    ONHOLD      = 'onhold'
    DROPPED     = 'dropped'
    PLANTOWATCH = 'plantowatch'
    PLANTOREAD  = 'plantoread'
