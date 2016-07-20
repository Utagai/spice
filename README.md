<p align="center"><img src="rsrc/horo_banner.png"></img></p>

## An Introduction

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

## Install

```bash
$ pip install spice_api
```

## Here's how to use it 

```python
import spice_api as spice

def main():
	creds = spice.load_auth_from_file('auth') #or spice.init_auth(username, pw)
	search_results = spice.search('Spice and Wolf', spice.get_medium('anime'))
	print(results[0].title) # > Ookami to Koushinryou
	saw_id = results[0].id # > 2966
	
	#mal sees everything as anime or manga, so novels are considered manga.
	saw_novel = spice.search_id(saw_id, spice.get_medium('manga'))
	print(saw_novel.title) # > Ookami to Koushinryou
	print(saw_novel.chapters) # > 0
	print(saw_novel.volumes) # > 18
	
	#get a fresh anime data object to fill in, and then push to your list
	saw_data = spice.get_blank(spice.get_medium('anime'))
	saw_data.episodes = 10 #you've watched 10 eps
	saw_data.status = spice.get_status('watching') #you're still watching
	saw_data.score = 9 #your rating
	saw_data.tags = ['Holo is the best.'] #tags
	#there are many other fields you can fill in, but this is enough.
	spice.update(saw_data, saw_id, spice.get_medium('anime')) #update your list.

	your_list = spice.get_list(spice.get_medium('anime')) #get your list (no args)
	other_anime_list = spice.get_list(spice.get_medium('anime'), 'Pickleplatter') #someone else's list
	
	print(your_list.avg_score()) # > mean 
	print(your_list.p_var()) # > variance
	print(your_list.get_num_status(spice.get_status_num('watching'))) #number of shows you're watching
	print(your_list.compatibility(other_anime_list)) # > you and your friend's compatibility score

```

## What's left
* Add more information to Anime() and Manga() objects through webscraping.
* Add more list comparison methods.
* Make README even more pretty.
