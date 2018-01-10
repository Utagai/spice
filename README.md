<p align="center"><img src="rsrc/horo_banner.png"></img></p>

# An Introduction

The [Official MyAnimeList API](http://myanimelist.net/modules.php?go=api) needs lots of work and is pretty annoying to use. Here are some of the many issues:
* Some of the documentation is just straight up incorrect (perhaps it was correct sometime ago).
* There are MySQL bugs on MAL's end that must be circumvented.
* There are severe limitations in what the API allows you to do, forcing the programmer's hand to write ugly scraping code.
* Some of the ways to do simple things like updating an anime on a user's list requires an esoteric knowledge of MAL URLs/queries that are no where on the documentation.
* The Official MAL API fails to provide consistent behavior.
	- e.g. When sending too many requests, the Official MAL API has unpredictable
	behavior.

Work and/or further development on it seems like a lost cause, since the developer(s) have far more pressing concerns with the site.

This API aims to provide an easy to use Python API that wraps around MAL's
REST-API so that you don't have to experience any headaches.

Name inspired by [Horo/Holo](http://myanimelist.net/character/7373/Holo) from [Spice and Wolf](http://myanimelist.net/anime/2966/Ookami_to_Koushinryou?q=Spice%20and%20Wolf).

API inspired by other attempts (which made their own REST API wrapper, while this one uses a pure Python implementation), such as [crobert22](https://github.com/croberts22)'s [Railgun](https://github.com/croberts22/railgun) and [chuyeow](https://github.com/chuyeow)'s [myanimelist-api](https://github.com/chuyeow/myanimelist-api).

# Install
Python 2:
```bash
$ pip install spice_api
```
Python 3:
```bash
$ pip3 install spice_api
```

# Documentation

**Authorization**:
+ from file: `creds = spice_api.load_auth_from_file('filename')`
+ inline: `creds = spice_api.init_auth("username","password")`


**Searching**:
+ search by name: You can use `spice_api.search(title,spice_api.getmedium("anime/manga"),credentials)` to search for an anime or manga. This returns a list of [Anime](#anime) or [Manga](#manga) objects by relevance to the search query.
+ search by id: If you already know the MAL id of an anime or manga, you can use use `spice_api.search_id(id,spice_api.getmedium("anime/manga"),credentials)`, to return the [Anime](#anime) or [Manga](#manga) object relevant.


**Updating your list**:
1. create blank Anime or Manga object `anime = spice.get_blank(spice.get_medium('anime'))`
2. Fill in fields like:
```python
saw_data.episodes = 10 #you've watched 10 eps
saw_data.status = spice_api.get_status('watching') #you're still watching
saw_data.score = 9 #your rating
saw_data.tags = ['Holo is the best.'] #tags
```
3. Push the update with `spice_api.update(saw_data, saw_id, spice.get_medium('anime'), creds)`

**Getting lists**


Referencing a [List](#list) object is as easy as `spice_api.get_list(spice.get_medium('anime'), 'username', creds)`


**Anime Object** <a name="anime"></a>
The Anime object has a number of attributes:
- `anime.id`, the MAL ID of the anime, used with `search_id` and `update` methods.
- `anime.title`, the title of the anime
- `anime.english`, english name of the anime, if applicable
- `anime.episodes`, number of episodes *NOTE: 0 if and only if number is unknown*
- `anime.score`, The rating of the anime.
- `anime.anime_type`, The type of anime ( Movie, ONA, OVA, TV, Special)
- `anime.status`, The anime status (Currently airing, Finished Airing, Not yet Aired)
- `anime.dates`, tuple of anime start and end dates (YYYY-MM-DD) *NOTE 0000-00-00 if and only if date is unknown*
- `anime.synopsis`, MAL synopsis of anime
- `anime.image_url`, the cover image's url.



**Manga Object**  <a name="manga"></a>

***NOTE**: Novels are also treated as manga.*

The manga object has similar attributes:
- `manga.id`, see `anime.id`
- `manga.title`, see `anime.title`
- `manga.english`, english name of the manga, if applicable
- `manga.chapters`, number of chapters in the manga  *NOTE: 0 if and only if number is unknown*
- `manga.volume`, the number of volumes in this manga. *NOTE: 0 if and only if number is unknown*
- `manga.score`, manga's rating
- `manga.manga_type`, format of manga (Manga, one-shot, manhwa, manhua, doujinshi, novel)
- `manga.status`, in what state the manga is in (e.g. Publishing, Finished)
- `manga.dates`, tuple of start and end date of publishing *NOTE 0000-00-00 if and only if date is unknown*
- `manga.synopsis`, synopsis of manga
- `manga.image_url`, cover image url

**List object** <a name= "list"></a>
This object encapsulates an anime *or* manga list. It has attributes :
- `mlist.medium`, whether it's an anime or manga list
- `mlist.raw_data`, raw xml data of the list
- `mlist.anime/manga_list`, dictionary containing 5 keys whose values contain 5 lists according to the key:
	+ "watching"/"reading" - all manga/anime that are being read or watched
	+ "completed"
	+ "onhold"
	+ "dropped"
	+ "plantowatch"
	e.g - `mlist.anime/manga_list[completed]` - returns all completed anime/manga in the list.
	
	
This object also includes some probably useless but potentially useful methods to analyze lists:
- `mlist.avg_score()` - average score
- `mlist.median_score()` - median score (score at approximately/exactly the 50th percentile)
- `mlist.mode_score()` - mode score (most often-appearing score)
- `mlist.extremes()` - extreme scores (high, low)
- `mlist.p_stddev()` - standard deviation
- `mlist.p_var()` - variance (square of standard deviation)
- `mlist.get_total()` - sum of scores
- `mlist.get_days()` - days spent watching
- `mlist.compatibility(otherlist)` - [pearson correlation](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) in percent of how high both of you rated the same anime/manga

***NOTE**: Raises ValueError if lists are of different medium type.*


# What's Left
* Add more information to Anime() and Manga() objects through webscraping.
* Add more list comparison methods.
* Make README even more pretty.
