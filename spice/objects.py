## A py module for objects.
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

''' A py module for objects.

WARN: This module is not meant to be used in any way besides in the internals of
the spice API source code.

This module defines the objects: Anime, Manga, AnimeData, MangaData and MediumList.
Anime and Manga are Mediums, so MediumList captures both Anime and MangaLists.

Anime and Manga objects are packages of parsed XML data for an anime or manga
respectively.

AnimeData and MangaData objects are packages of anime or manga respectively that
is intended to be pushed to MAL in an operation request such as adding, updating or
deleting.

MediumLists are returned from requests about a user's Anime/MangaList(s).
'''

import spice
import helpers
import stats
import constants
import requests
from bs4 import BeautifulSoup

class Anime:
    '''An object that encapsulates an Anime.

    Uses properties so that it doesn't parse through XML
    unnecessarily, and instead,  does so only when immediately
    necessary.

    Has properties:
        id         - The id of the anime.
        title      - The title of the anime.
        english    - The english name of the anime, if applicable.
        episodes   - The number of episodes in this anime.
        score      - The rating of the anime.
        anime_type - The type of anime (e.g. movie, ONA, etc)
        status     - In what state the anime is in (e.g. airing, finished, etc)
        dates      - A tuple of start and end dates of airing of the anime.
        synopsis   - The synopsis text of the anime.
        image_url  - A url to the anime's cover image.
    '''
    def __init__(self, anime_data):
        self.raw_data = anime_data
        #these are generated when they are called, so we save
        #computation when it is not needed.
        self._id         = None
        self._title      = None
        self._english    = None
        self._episodes   = None
        self._score      = None
        self._anime_type = None
        self._status     = None
        self._dates      = None
        self._synopsis   = None
        self._image_url  = None
        self._rewatches  = None
        self._rewatch_ep = None

    @property
    def id(self):
        if self._id is None:
            id_val = self.raw_data.id
            if id_val is None: #AnimeList Anime data.
                id_val = self.raw_data.series_animedb_id
            self._id = id_val.text
        return self._id

    @property
    def title(self):
        if self._title is None:
            title_val = self.raw_data.title
            if title_val is None:
                title_val = self.raw_data.series_title
            self._title = title_val.text
        return self._title

    @property
    def english(self):
        if self._english is None:
            english_val = self.raw_data.english
            if english_val is None:
                return None
            self._english = english_val.text
        return self._english

    @property
    def episodes(self):
        if self._episodes is None:
            episodes_val = self.raw_data.episodes
            if episodes_val is None:
                episodes_val = self.raw_data.my_watched_episodes
            self._episodes = episodes_val.text
        return self._episodes

    @property
    def score(self):
        if self._score is None:
            score_val = self.raw_data.score
            if score_val is None:
                score_val = self.raw_data.my_score
            self._score = score_val.text
        return self._score

    @property
    def anime_type(self):
        if self._type is None:
            type_val = self.raw_data.type
            if type_val is None:
                return None
            self._type = type_val.text
        return self._type

    @property
    def status(self):
        if self._status is None:
            status_val = self.raw_data.status
            if status_val is None:
                status_val = self.raw_data.my_status
            self._status = status_val.text
        return self._status

    @property
    def dates(self):
        if self._dates is None:
            start_val = self.raw_data.start_date
            end_val = self.raw_data.end_date
            if start_val is None:
                start_val = self.raw_data.my_start_date
                end_val = self.raw_data.my_end_date
            self._dates = (start_val.text, end_val.text)
        return self._dates

    @property
    def synopsis(self):
        if self._synopsis is None:
            synopsis_val = self.raw_data.synopsis
            if synopsis_val is None:
                return None
            self._synopsis = synopsis_val.text
        return self._synopsis

    @property
    def image_url(self):
        if self._image_url is None:
            image_val = self.raw_data.image
            if image_val is None:
                image_val = self.raw_data.series_image
            self._image_url = image_val.text
        return self._image_url

    @property
    def rewatches(self):
        if self._rewatches is None:
            rewatch_val = self.raw_data.my_rewatching
            if rewatch_val is None:
                return None
            self._rewatches = rewatch_val.text
            return self._rewatches

    @property
    def rewatch_ep(self):
        if self._rewatch_ep is None:
            rewatch_ep_val = self.raw_data.my_rewatching_ep
            if rewatch_ep_val is None:
                return None
            self._rewatch_ep = rewatch_ep_val.text
            return self._rewatch_ep

class AnimeData:
    '''An object for packaging data required for operations on AnimeLists

    Has attributes:
        episodes - The number of episodes in this anime that you've watched.
        status   - Are you: watching(1), completed(2), on-hold(3), dropped(4),
                          plan-to-watch(6) <- Don't ask me, ask MAL devs >_>.
        score    - The rating of the anime.
        dates    - A tuple of start and end dates of airing of the anime.
        tags     - The tags to put on your list for this Anime.
        The rest are not necessary for operations and can be left blank.
    '''
    def __init__(self):
        self.episodes = 0
        self.status = 0
        self.score = 0
        self.storage_type = ''
        self.storage_value = ''
        self.times_rewatched = ''
        self.rewatch_value = ''
        self.dates = ('', '')
        self.priority = ''
        self.set_discuss = ''
        self.set_rewatch = ''
        self.comments = ''
        self.fansub_group = ''
        self.tags = []

    def to_xml(self):
        return '''<?xml version='1.0' encoding='UTF-8'?>
                <entry>
                    <episode>{}</episode>
                    <status>{}</status>
                    <score>{}</score>
                    <storage_type>{}</storage_type>
                    <storage_value>{}</storage_value>
                    <times_rewatched>{}</times_rewatched>
                    <rewatch_value>{}</rewatch_value>
                    <date_start>{}</date_start>
                    <date_finish>{}</date_finish>
                    <priority>{}</priority>
                    <enable_discussion>{}</enable_discussion>
                    <enable_rewatching>{}</enable_rewatching>
                    <comments>{}</comments>
                    <fansub_group>{}</fansub_group>
                    <tags>{}</tags>
                </entry>'''.format(self.episodes, self.status,
                                   self.score, self.storage_type,
                                   self.storage_value, self.times_rewatched,
                                   self.rewatch_value, self.dates[0],
                                   self.dates[1], self.priority,
                                   self.set_discuss, self.set_rewatch,
                                   self.comments, self.fansub_group,
                                   str(self.tags)[1:-1].replace('\'', ''));


class Manga:
    '''An object that encapsulates an Manga.

    Uses properties so that it doesn't parse through XML
    unnecessarily, and instead,  does so only when immediately
    necessary.

    Has properties:
        id         - The id of the manga.
        title      - The title of the manga.
        english    - The english name of the manga, if applicable.
        chapter    - The number of chapters in this manga.
        volume     - The number of volumes in this manga.
        score      - The rating of the manga.
        manga_type - The type of manga (e.g. movie, ONA, etc)
        status     - In what state the manga is in (e.g. airing, finished, etc)
        dates      - A tuple of start and end dates of airing of the manga.
        synopsis   - The synopsis text of the manga.
        image_url  - A url to the manga's cover image.
    '''
    def __init__(self, manga_data):
        self.raw_data     = manga_data
        self._id          = None
        self._title       = None
        self._english     = None
        self._chapters    = None
        self._volumes     = None
        self._score       = None
        self._type        = None
        self._status      = None
        self._dates       = None
        self._synopsis    = None
        self._image_url   = None
        self._rereads     = None
        self._reread_chap = None

    @property
    def id(self):
        if self._id is None:
            id_val = self.raw_data.id
            if id_val is None:
                id_val = self.raw_data.series_mangadb_id
            self._id = id_val.text
        return self._id

    @property
    def title(self):
        if self._title is None:
            title_val = self.raw_data.title
            if title_val is None:
                title_val = self.raw_data.series_title
            self._title = title_val.text
        return self._title

    @property
    def english(self):
        if self._english is None:
            english_val = self.raw_data.english
            if english_val is None:
                return None
            self._english = english_val.text
        return self._english

    @property
    def chapters(self):
        if self._chapters is None:
            chapter_val = self.raw_data.chapters
            if chapter_val is None:
                chapter_val = self.raw_data.my_read_chapters
            self._chapters = chapter_val.text
        return self._chapters

    @property
    def volumes(self):
        if self._volumes is None:
            volumes_val = self.raw_data.volumes
            if volumes_val is None:
                volumes_val = self.raw_data.my_read_volumes
            self._volumes = volumes_val.text
        return self._volumes

    @property
    def score(self):
        if self._score is None:
            score_val = self.raw_data.score
            if score_val is None:
                score_val = self.raw_data.my_score
            self._score = score_val.text
        return self._score

    @property
    def manga_type(self):
        if self._type is None:
            manga_type_val = self.raw_data.type
            if manga_type_val is None:
                return None
            self._type = manga_type_val.text
        return self._type

    @property
    def status(self):
        if self._status is None:
            status_val = self.raw_data.status
            if status_val is None:
                status_val = self.raw_data.my_status
            self._status = status_val.text
        return self._status

    @property
    def dates(self):
        if self._dates is None:
            start_val = self.raw_data.start_date
            end_val = self.raw_data.end_date
            if start_date is None:
                start_val = self.raw_data.my_start_date
                end_val = self.raw_data.my_end_date
            self._dates = (start_val.text, end_val.text)
        return self._dates

    @property
    def synopsis(self):
        if self._synopsis is None:
            synopsis_val = self.raw_data.synopsis
            if synopsis_val is None:
                return None
            self._synopsis = synopsis_val.text
        return self._synopsis

    @property
    def image_url(self):
        if self._image_url is None:
            image_val = self.raw_data.image
            if image_val is None:
                image_val = self.raw_data.series_image
            self._image_url = image_val.text
        return self._image_url

class MangaData:
    '''An object for packaging data required for operations on MangaLists

    Has attributes:
        chapters - The number of chapters in this manga that you've read.
        volume   - The volume in this manga that you've read.
        status   - Are you: reading(1), completed(2), on-hold(3), dropped(4),
                          plan-to-read(6) <- Don't ask me, ask MAL devs >_>.
        score    - The rating of the manga.
        dates    - A tuple of start and end dates of airing of the manga.
        tags     - The tags to put on your list for this manga.
        The rest are not necessary for operations and can be left blank.
    '''
    def __init__(self):
        self.chapters = 0
        self.volume = 0
        self.status = 0
        self.score = 0
        self.times_reread = ''
        self.reread_value = ''
        self.dates = ('', '')
        self.priority = ''
        self.set_discuss = ''
        self.set_reread = ''
        self.comments = ''
        self.scan_group = ''
        self.tags = []
        self.retail_volumes = ''

    def to_xml(self):
        return '''<?xml version='1.0' encoding='UTF-8'?>
                <entry>
                    <chapter>{}</chapter>
                    <volume>{}</volume>
                    <status>{}</status>
                    <score>{}</score>
                    <times_reread>{}</times_reread>
                    <reread_value>{}</reread_value>
                    <date_start>{}</date_start>
                    <date_finish>{}</date_finish>
                    <priority>{}</priority>
                    <enable_discussion>{}</enable_discussion>
                    <enable_rereading>{}</enable_rereading>
                    <comments>{}</comments>
                    <scan_group>{}</scan_group>
                    <tags>{}</tags>
                    <retail_volumes>{}</retail_volumes>
                </entry>'''.format(self.chapters, self.volumes,
                                   self.status, self.score, self.times_reread,
                                   self.reread_value, self.dates[0],
                                   self.dates[1], self.priority,
                                   self.set_discuss, self.set_reread,
                                   self.comments, self.scan_group,
                                   str(self.tags)[1:-1].replace('\'', ''),
                                   self.retail_volumes);

class MediumList:
    '''An object that encapsulates an Anime or MangaList.


    Has attributes:
        medium             - [Anime or Manga]List.
        raw_data           - The raw XML data that this MediumList is made from.
        anime/manga_list   - The dictionary containing the 5 lists for anime...
                                ...WATCHING/READING (keys: 'watching'/'reading')
                                ...COMPLETED (key: 'completed')
                                ...ONHOLD (key: 'onhold')
                                ...DROPPED (key: 'dropped')
                                ...PLANTOWATCH (key: 'plantowatch')

    '''
    def __init__(self, medium, list_data):
        self.medium = medium
        self.raw_data = list_data
        self.days = 0.0
        if self.medium == spice.Medium.ANIME:
            self.medium_list = {spice.Key.WATCHING:[], spice.Key.COMPLETED:[],
                                spice.Key.ONHOLD:[], spice.Key.DROPPED:[],
                                spice.Key.PLANTOWATCH:[]}
        elif self.medium == spice.Medium.MANGA:
            self.medium_list = {spice.Key.READING:[], spice.Key.COMPLETED:[],
                                spice.Key.ONHOLD:[], spice.Key.DROPPED:[],
                                spice.Key.PLANTOREAD:[]}
        else:
            #not sure what the best thing to do is... default to anime?
            raise ValueError(constants.INVALID_MEDIUM)

        self.load()

    def load(self):
        list_soup = self.raw_data
        if self.medium == spice.Medium.ANIME:
            list_items = list_soup.findAll('anime')
            for item in list_items:
                status = helpers.find_key(item.my_status.text, self.medium)
                status_list = self.medium_list[status]
                status_list.append(Anime(item))
        else: #we are guaranteed to, at this point, have a valid medium
            list_items = list_soup.findAll('manga')
            for item in list_items:
                status = helpers.find_key(item.my_status.text, self.medium)
                status_list = self.medium_list[status]
                status_list.append(Manga(item))

    def get_mediums(self):
        all_entries_in_list = []
        for status, entries in self.medium_list.iteritems():
            all_entries_in_list += entries

        return all_entries_in_list

    def get_scores(self):
        all_entries = self.get_mediums()
        ptw = str(spice.StatusNumber.PLANTOWATCH)
        return [int(entry.score) for entry in all_entries if entry.status != ptw]

    def get_ids(self):
        all_entries = self.get_mediums()
        return [int(entry.id) for entry in all_entries]

    def get_titles(self):
        all_entries = self.get_mediums()
        return [entry.title for entry in all_entries]

    def get_status(self, status):
        status_key = helpers.find_key_num(helpers.det_key(status, self.medium))
        all_entries = self.get_mediums()
        return [int(entry.id) for entry in all_entries if entry.status == str(status_key)]

    def get_score(self, score):
        all_entries = self.get_mediums()
        return [int(entry.id) for entry in all_entries if entry.score == str(score)]

    def avg_score(self):
        return stats.mean(self.get_scores())

    def median_score(self):
        return stats.median(self.get_scores())

    def mode_score(self):
        return stats.mode(self.get_scores())

    def extremes(self):
        return stats.extremes(self.get_scores())

    def p_stddev(self):
        return stats.p_stddev(self.get_scores())

    def p_var(self):
        return stats.p_var(self.get_scores())

    def get_num_status(self, status):
        status_key = helpers.det_key(status, self.medium)
        return len(self.medium_list[status_key])

    def get_total(self):
        total_count = len(self.get_scores())
        if self.medium == spice.Medium.ANIME:
            total_count += len(self.medium_list[spice.Key.PLANTOWATCH])
        else:
            total_count += len(self.medium_list[spice.Key.PLANTOREAD])

        return total_count

    def get_days(self):
        user_info = self.raw_data.myinfo
        self.days = float(user_info.user_days_spent_watching.text)
        return self.days

    def exists(self, id):
        all_entries = self.get_ids()
        if id in all_entries:
            return True
        else:
            return False

    def exists_as_status(self, id, status):
        all_entries_id = self.get_ids()
        all_entries_status = self.get_status(status)
        if id in all_entries_id and id in all_entries_status:
            return True
        else:
            return False

    def score_diff(self):
        user_avg = self.avg_score()
        global_resp = requests.get(constants.MALGRAPH_GLOBAL)
        global_soup = BeautifulSoup(global_resp.text, 'html.parser')
        subjects = global_soup.findAll('span', {'class':'subject'})
        global_avg_subjects = []
        for subject in subjects:
            if '%' in subject.text:
                continue
            elif '.' not in subject.text:
                continue
            else:
                global_avg_subjects.append(subject.text)

        if self.medium == spice.Medium.ANIME:
            return user_avg - float(global_avg_subjects[0])
        else:
            return user_avg - float(global_avg_subjects[1])

    def compatibility(self, other_list):
        if self.medium != other_list.medium:
            raise ValueError(INVALID_LIST_MATCH)
        #linear time set intersection karl pearson coefficient correlation
        plan_to_watch = str(spice.StatusNumber.PLANTOWATCH)
        all_x = self.get_mediums()
        x_ids = [entry.id for entry in all_x if entry.status != plan_to_watch]
        x_scores = self.get_scores()
        x_map = dict(zip(x_ids, x_scores))

        all_y = other_list.get_mediums()
        y_ids = [entry.id for entry in all_y if entry.status != plan_to_watch]
        y_scores = other_list.get_scores()
        y_map = dict(zip(y_ids, y_scores))

        common_mediums = set.intersection(set(x_ids), set(y_ids))

        x_data = []
        y_data = []

        for medium in common_mediums:
            x_data.append(x_map[medium])
            y_data.append(y_map[medium])

        pearson_coeff = stats.karl_pearson2(x_data, y_data)
        return pearson_coeff
