import pandas as pd
import numpy as np


def into_bins(data, bins, file_name):
    new_data = data.copy()
    #new_data.drop(labels='Unnamed: 0', axis=1, inplace=True)
    skip_cols = ['gender', 'race', 'race_o', 'samerace', 'field', 'decision', 'Unnamed: 0']
    cols = list(new_data.columns)
    for col in cols:
        if col not in skip_cols:
            new_data[col], interval = pd.cut(x=data[col], bins=bins-1, right=True, retbins=True)
            print('{0}: {1}'.format(col, interval))



    new_data.to_csv(file_name, index=False)



def split(data, test_file, training_file):
    test_data = data.sample(frac=0.2, random_state=47)
    test_data.to_csv(test_file,index=False)
    training_data = data.drop(test_data.index)
    training_data.to_csv(training_file,index=False)



if __name__ == '__main__':
    data = pd.read_csv('./dating.csv')
    into_bins(data=data, bins = 5, file_name='./dating-binned.csv')
    data_bined = pd.read_csv('./dating-binned.csv')
    split(data=data_bined, test_file='./testSet.csv', training_file='./trainingSet.csv')