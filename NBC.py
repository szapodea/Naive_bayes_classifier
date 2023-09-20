import numpy as np
import pandas as pd
import scipy as sc


def pre_process(file):
    data = pd.read_csv(file)
    data = replace_quotes(data=data)
    data = to_lowercase(data=data)
    data.to_csv('./after_lowercase.csv')
    data = numeric_values(data=data)

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


# function that encodes 4 dimensions into numerical values
# also outputs the value assigned to certain labels
def numeric_values(data):
    RACE = 4 # column of race
    RACE_O = 5 # column of race_o
    GENDER = 1 # column of gender
    FIELD = 9 # column of field

    data = data.sort_values(by=['race'])
    race_dict = {}
    cnt = 0

    for row in data.itertuples():
        if row[RACE] not in race_dict:
            race_dict[row[RACE]] = cnt
            cnt += 1

    data = data.replace({'race': race_dict})

    data = data.sort_values(by=['race_o'])
    raceo_dict = {}
    cnt = 0

    for row in data.itertuples():
        if row[RACE_O] not in raceo_dict:
            raceo_dict[row[RACE_O]] = cnt
            cnt += 1

    data = data.replace({'race_o': raceo_dict})

    data = data.sort_values(by=['gender'])
    gender_dict = {}
    cnt = 0

    for row in data.itertuples():
        if row[GENDER] not in gender_dict:
            gender_dict[row[GENDER]] = cnt
            cnt += 1

    data = data.replace({'gender': gender_dict})

    data = data.sort_values(by=['field'])
    field_dict = {}
    cnt = 0

    for row in data.itertuples():
        if row[FIELD] not in field_dict:
            field_dict[row[FIELD]] = cnt
            cnt += 1

    data = data.replace({'field': field_dict})

    print('Value assigned for male in column gender: {0}'.format(gender_dict['male']))
    print('Value assigned for European/Caucasian-American in column race: {0}.'.format(race_dict['European/Caucasian-American']))
    print('Value assigned for Latino/Hispanic American in column race_o: {0}.'.format(raceo_dict['Latino/Hispanic American']))
    print('Value assigned for law in column field: {0}'.format(field_dict['law']))
    
    return data



if __name__ == '__main__':
    pre_process('dating-full.csv')