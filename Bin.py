import pandas as pd
import numpy as np

ages = ['age', 'age_o']
zero_to_ten = ['important_same_race', 'important_same_religion', 'attractive', 'sincere', 'intelligence', 'funny',
               'ambition', 'attractive_partner', 'sincere_partner', 'intelligence_partner', 'funny_partner',
               'ambition_partner', 'shared_interests_partner', 'sports', 'tvsports', 'exercise', 'dining', 'museums'
                                                                                                           'art',
               'hiking', 'gaming', 'clubbing', 'reading', 'tv', 'theater', 'movies', 'concerts', 'music',
               'shopping', 'yoga', 'expected_happy_with_sd_people', 'like']
neg_to_pos_one = ['interests_correlate']
def set_max(data):
    for col in list(data.columns):
        if col in ages:
            data.loc[:, col].clip(lower=18, upper=58, inplace=True)
        if col in zero_to_ten:
            data.loc[:, col].clip(lower=0, upper=10,inplace=True)
        if col in neg_to_pos_one:
            data.loc[:, col].clip(lower=-1, upper=1, inplace=True)

    return data


def into_bins(data, bins, file_name):
    new_data = data.copy()
    #new_data.drop(labels='Unnamed: 0', axis=1, inplace=True)
    skip_cols = ['gender', 'race', 'race_o', 'samerace', 'field', 'decision', 'Unnamed: 0']
    cols = list(new_data.columns)
    for col in cols:
        if col not in skip_cols:
            new_data[col], interval = pd.cut(x=data[col], bins=bins, right=True, retbins=True)
            counts = new_data[col].value_counts(sort=False)
            # need to uncomment this line
            print('{0}: {1}'.format(col, counts.values))


    new_data.to_csv(file_name, index=False)



def split(data, test_file, training_file):
    test_data = data.sample(frac=0.2, random_state=47)
    test_data.to_csv(test_file, index=False)
    training_data = data.drop(test_data.index)
    training_data.to_csv(training_file, index=False)



if __name__ == '__main__':
    data = pd.read_csv('./dating.csv')
    data = set_max(data=data)
    into_bins(data=data, bins=5, file_name='./dating-binned.csv')
    data_bined = pd.read_csv('./dating-binned.csv')
    split(data=data_bined, test_file='./testSet.csv', training_file='./trainingSet.csv')