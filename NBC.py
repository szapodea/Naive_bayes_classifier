import numpy as np
import pandas as pd
import scipy as sc




def pre_process(file):
    columns = ['gender', 'age', 'age_o', 'race', 'race_o', 'samerace', 'importance_same_race',
                   'importance_same_religion', 'field', 'pref_o_attractive', 'pref_o_sincere',
                   'pref_o_intelligence', 'pref_o_funny', 'pref_o_ambitious', 'pref_o_shared_interests',
                   'attractive_important', 'sincere_important', 'intelligence_important', 'funny_important',
                   'ambition_important', 'shared_interests_important', 'attractive', 'sincere', 'intelligence',
                   'funny', 'ambition', 'attractive_partner', 'sincere_partner', 'intelligence_parter', 'funny_partner',
                   'ambition_partner', 'shared_interests_partner', 'sports', 'tvsports', 'exercise', 'dining', 'museums',
                   'art', 'hiking', 'gaming', 'clubbing', 'reading', 'tv', 'theater', 'movies', 'concerts', 'music',
                   'shopping', 'yoga', 'interests_correlate', 'expected_happy_with_sd_people', 'like', 'decision']
    data = pd.read_csv(file, usecols=columns)
    data = replace_quotes(data=data)

# function that strips single quotes (') of three dimensions of the data set.
# also counts the number of datapoints that have quotes replaced and prints them
def replace_quotes(data):
    replace_cnt = 0
    for i in range(len(data['race'])):
        if '\'' in data['race'][i]:
            data['race'][i] = data['race'][i].replace('\'', '')
            replace_cnt += 1

    for row in data['race_o']:
        if '\'' in row:
            row = row.replace('\'', '')
            replace_cnt += 1
    for row in data['field']:
        if '\'' in row:
            row = row.replace('\'', '')
            replace_cnt += 1

    print("Quotes removed from {0} cells.".format(replace_cnt))
    print(data['race'])
    print(data['race_o'])
    print(data['field'])

    return data




if __name__ == '__main__':
    pre_process('dating-full.csv')