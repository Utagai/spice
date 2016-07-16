from bs4 import BeautifulSoup
import requests
import spice_mal as spice

import sys, os

#sys.path.insert(0, '/home/may/Dropbox/Programming/spice/spice')

def main():
    creds = spice.load_auth_from_file('auth')
    print(creds)
    results = spice.search('Spice and Wolf', spice.get_medium('anime'))
    print(results[0].title)
    saw_novel = spice.search_id(9115, spice.get_medium('manga'))
    print(saw_novel.raw_data)
    print(saw_novel.title)
    print(saw_novel.chapters)
    print(saw_novel.volumes)

    saw_data = spice.get_blank(spice.get_medium('anime'))
    saw_data.episodes = 10
    saw_data.status = spice.get_status('watching')
    saw_data.score = 9
    saw_data.tags = ['holo is the best']
    spice.update(saw_data, 2966, spice.get_medium('anime'))

    #shokugeki_data = spice.get_blank(spice.get_medium('manga'))
    #shokugeki_data.chapters = 13
    #shokugeki_data.volumes = 1
    #shokugeki_data.status = 1
    #shokugeki_data.score = 8
    #spice.update(shokugeki_data, 45757, spice.get_medium('manga'))

    #anime_list = spice.get_list(spice.get_medium('ANIME'))
    #print(anime_list.avg_score())
    #print(anime_list.median_score())
    #print(anime_list.mode_score())
    #print(anime_list.extremes())
    #print(anime_list.p_stddev())
    #print(anime_list.p_var())
    #print(anime_list.get_num_status(1))
    #print(anime_list.get_total())
    #print(anime_list.get_days())
    #print(anime_list.exists(11734))
    #print(len(anime_list.get_ids()))
    #print(len(anime_list.get_titles()))
    #print(anime_list.get_status(1))
    #print(anime_list.get_score(10))
    #print(anime_list.exists_as_status(11734, 1))
    #print(anime_list.score_diff())
    #anime_list2 = spice.get_list(spice.get_medium('ANIME'), 'Pickleplatter')
    #print("Similarity coefficient: {}".format(anime_list.compatibility(anime_list2)))

if __name__ == '__main__':
    main()
