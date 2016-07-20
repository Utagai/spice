from bs4 import BeautifulSoup
import requests

import sys, os

from time import sleep
sys.path.insert(0, '/home/may/Dropbox/Programming/spice/')

import spice_api as spice

def main():
    creds = spice.load_auth_from_file('auth')
    print(creds)
    results = spice.search('Re:Zero Kara Hajimeru Isekai Seikatsu', spice.get_medium('anime'))
    print(results[0].title)
    souma = spice.search_id(1, spice.get_medium('manga'))
    print(souma.raw_data)
    print(souma.title)
    print(souma.chapters)
    print(souma.volumes)
    re_zero_data = spice.get_blank(spice.get_medium('anime'))
    re_zero_data.episodes = 0
    re_zero_data.status = spice.get_status('reading')
    re_zero_data.score = 8
    re_zero_data.tags = ['this the first time a show that made me cringe']
    for x in range(10):
        spice.update(re_zero_data, 31240, spice.get_medium('anime'))
        re_zero_data.episodes += 1
        print("Sleeping for 5 seconds...")
        sleep(1)
        print("1")
        sleep(3)
        print("4")
        sleep(1)
        print("5")

    return

    shokugeki_data = spice.get_blank(spice.get_medium('manga'))
    shokugeki_data.chapters = 13
    shokugeki_data.volumes = 1
    shokugeki_data.status = 1
    shokugeki_data.score = 8
    spice.update(shokugeki_data, 45757, spice.get_medium('manga'))

    anime_list = spice.get_list(spice.get_medium('ANIME'))
    print(anime_list.avg_score())
    print(anime_list.median_score())
    print(anime_list.mode_score())
    print(anime_list.extremes())
    print(anime_list.p_stddev())
    print(anime_list.p_var())
    print(anime_list.get_num_status(1))
    print(anime_list.get_total())
    print(anime_list.get_days())
    print(anime_list.exists(11734))
    print(len(anime_list.get_ids()))
    print(len(anime_list.get_titles()))
    print(anime_list.get_status(1))
    print(anime_list.get_score(10))
    print(anime_list.exists_as_status(11734, 1))
    print(anime_list.score_diff())
    anime_list2 = spice.get_list(spice.get_medium('ANIME'), 'Pickleplatter')
    print("Similarity coefficient: {}".format(anime_list.compatibility(anime_list2)))

if __name__ == '__main__':
    main()
