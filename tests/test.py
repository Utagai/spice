from bs4 import BeautifulSoup
import requests
import spice

def main():
    creds = spice.load_auth_from_file('auth')
    #print(creds)
    #results = spice.search('Re:Zero Kara Hajimeru Isekai Seikatsu', spice.Medium.ANIME)
    #print(results[0].title)
    #souma = spice.search_id(1, spice.Medium.MANGA)
    #print(souma.raw_data)
    #print(souma.title)
    #print(souma.chapters)
    #print(souma.volumes)
    #re_zero_data = spice.get_blank(spice.Medium.ANIME)
    #re_zero_data.episodes = 15
    #re_zero_data.status = 1
    #re_zero_data.score = 8
    #re_zero_data.tags = ['this the first time a show that made me cringe']

    #shokugeki_data = spice.get_blank(spice.Medium.MANGA)
    #shokugeki_data.chapters = 19
    #shokugeki_data.volumes = 1
    #shokugeki_data.status = spice.Status.READING
    #shokugeki_data.score = 8
    #spice.update(shokugeki_data, 45757, spice.Medium.MANGA)

    anime_list = spice.get_list(spice.Medium.ANIME)
    #print(anime_list.avg_score())
    #print(anime_list.median_score())
    #print(anime_list.mode_score())
    #print(anime_list.extremes())
    #print(anime_list.p_stddev())
    #print(anime_list.p_var())
    #print(anime_list.get_num_status(spice.Key.READING))
    #print(anime_list.get_total())
    #print(anime_list.get_days())
    #print(anime_list.exists(11734))
    #print(len(anime_list.get_ids()))
    #print(len(anime_list.get_titles()))
    #print(anime_list.get_status(spice.StatusNumber.WATCHING))
    #print(anime_list.get_score(10))
    #print(anime_list.exists_as_status(11734, spice.StatusNumber.READING))
    #print(anime_list.score_diff())
    anime_list2 = spice.get_list(spice.Medium.ANIME, 'Pickleplatter')
    print("Similarity coefficient: {}".format(anime_list.compatibility(anime_list2)))

if __name__ == '__main__':
    main()
