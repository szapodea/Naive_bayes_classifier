import pandas as pd
import numpy as np


def into_bins(data):
    new_data = data.copy()
    #new_data.drop(labels='Unnamed: 0', axis=1, inplace=True)
    skip_cols = ['gender', 'race', 'race_o', 'samereace', 'field', 'decision', 'Unnamed: 0']
    cols = list(new_data.columns)
    lines = 0
    for col in cols:
        if col not in skip_cols:
            new_data[col], interval = pd.cut(x=data[col], bins=4, right=True, retbins=True)
            print('{0}:  {1}'.format(col, interval))
            lines+= 1

    print(lines)

    new_data.to_csv('./dating-binned.csv', index=False)



def split(data):
    test_data = data.sample(frac=0.2, random_state=47)
    test_data.to_csv('./testSet.csv')
    training_data = data.drop(test_data.index)
    training_data.to_csv('./training.csv')



if __name__ == '__main__':
    data = pd.read_csv('./dating.csv')
    into_bins(data=data)
    split(data=data)