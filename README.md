<p align="center"><img src="rsrc/horo_spice.png"></img></p>

## An Introduction

The [Official MyAnimeList API](http://myanimelist.net/modules.php?go=api) needs lots of work and is pretty annoying to use. Work and/or further development on it seems like a lost cause, since the developer(s) have far more pressing concerns with the site.

This API aims to provide an easy to use Python API that wraps around MAL's
REST-API.

Name inspired by [Horo/Holo](http://myanimelist.net/character/7373/Holo) from [Spice and Wolf](http://myanimelist.net/anime/2966/Ookami_to_Koushinryou?q=Spice%20and%20Wolf).

API inspired by other attempts (which made their own REST API wrapper, while this one uses a pure Python implementation), such as [crobert22](https://github.com/croberts22)'s [Railgun](https://github.com/croberts22/railgun) and [chuyeow](https://github.com/chuyeow)'s [myanimelist-api](https://github.com/chuyeow/myanimelist-api).

## Install (WIP)

```bash
$ pip install spice
```

## Here's how to use it (WIP)

```python
import spice

def main():
    spice.init_auth('username', 'password')
    saw_results_anime = spice.search('spice and wolf', spice.ANIME)
    for result in saw_results_anime:
    	print("{} : {} ({}) | {} episodes. Score: {}.".format(result.id,
															result.title,
															result.english,
															result.episodes,
															result.score)
    saw_season_one = spice.search_id(2966, spice.ANIME) #Spice and Wolf, Season 1

    saw_results_manga = spice.search('Ookami to Koushinryou', spice.MANGA)
    for result in saw_results_manga:
    	print("{} : {} ({}) | {} chapters, {} volumes. Score: {}.".format(result.id,
																		result.title,
																		result.english,
																		result.chapters,
																		result.volumes,
																		result.score)
    
    saw_data = spice.MangaData()
    saw_data.chapters = 4
    saw_data.volume = 2
    saw_data.status = 1 #reading
    saw_data.score = 9 #9/10
    
    spice.add(saw_data, 9115, spice.MANGA) #add manga to manga list.
    saw_data.chapters = 5 #read a chapter
    spice.update(saw_data, 9115, spice.MANGA) #update mangalist
    spice.delete(saw_data, 9115, spice.MANGA)

```
