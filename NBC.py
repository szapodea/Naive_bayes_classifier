import numpy as np
import pandas as pd
import scipy as sc


def pre_process(file):
    data = pd.read_csv(file)
    data = replace_quotes(data=data)
    data = to_lowercase(data=data)

# function that strips single quotes (') of three dimensions of the data set.
# also counts and outputs the number of datapoints that have quotes replaced
def replace_quotes(data):
    replace_cnt = 0
    for i in range(len(data.loc[:, 'race'])):
        if '\'' in data.loc[:, 'race'][i]:
            replace_cnt += 1
        if '\'' in data.loc[:, 'race_o'][i]:
            replace_cnt += 1
        if '\'' in data.loc[:, 'field'][i]:
            replace_cnt += 1

    print("Quotes removed from {0} cells.".format(replace_cnt))
    data['race'] = data['race'].str.replace('\'', '')
    data['race_o'] = data['race_o'].str.replace('\'', '')
    data['field'] = data['field'].str.replace('\'', '')
    return data

# function that sets all characters in field dimension to lowercase
# also counts and outputs the number of datapoints set to lowercase
def to_lowercase(data):
    lower_data = data['field'].str.lower()
    lower_cnt = 0
    for (lower, row) in zip(lower_data, data['field']):
        if lower != row:
            lower_cnt += 1
    print("Standardized {0} cells to lower case.".format(lower_cnt))
    data['field'] = lower_data

    return data




if __name__ == '__main__':
    pre_process('dating-full.csv')