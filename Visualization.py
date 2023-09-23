import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def visualize_gender(data):
    grouped = data.groupby('gender')
    females = grouped.get_group(0)
    males = grouped.get_group(1)
    barWidth = .3
    cols = ["attractive_important", "sincere_important", "intelligence_important",
            "funny_important", "ambition_important", "shared_interests_important"]
    male_means = []
    female_means = []

    for col in cols:
        male_means.append(np.mean(males[col]))
        female_means.append(np.mean(females[col]))


    fig = plt.subplots(figsize= (12, 8))

    br1 = np.arange(len(cols))
    br2 = [x + barWidth for x in br1]

    plt.bar(br1, male_means, color='blue', width=barWidth, label='Male Means')
    plt.bar(br2, female_means, color='red', width=barWidth, label='Female Means')

    plt.xlabel('Normalized Preference Scores of Participant', fontsize=15)
    plt.ylabel('Mean', fontsize=15)
    plt.xticks([r + barWidth - .15 for r in range(len(cols))], cols)

    plt.legend()
    plt.show()


def scatter_plots(data):
    cols = ['attractive_partner', 'sincere_partner', 'intelligence_partner',
            'funny_partner', 'ambition_partner', 'shared_interests_partner']

    distinct_vals = {}

    for col in cols:
        distinct_vals[col] = data[col].unique()
    '''
    print(distinct_vals['attractive_partner'])

    matching = data.loc[data['attractive_partner'] == 0]
    yes = matching['decision'].value_counts()
    print(dict(yes))
    yes = dict(yes)
    if 1 not in yes.keys():
        print(0)
    elif 1 not in yes.keys():
        print(1)
    else:
        print(yes[1]/(yes[0] + yes[1]))
    '''

    second_date_percent = []
    for col in cols:
        temp = {}
        for val in distinct_vals[col]:
            matching = data.loc[data[col] == val]
            cnt = matching['decision'].value_counts()
            cnt = dict(cnt)
            if 1 not in cnt.keys():
                temp[val] = 0
            elif 0 not in cnt.keys():
                temp[val] = 1
            else:
                temp[val] = cnt[1]/(cnt[0] + cnt[1])
        second_date_percent.append(temp)

    #print(second_date_percent)

    for col in range(len(cols)):
        #print(second_date_percent[col].keys())
        x = second_date_percent[col].keys()
        y = second_date_percent[col].values()
        print(x, y)
        plt.figure(cols[col])
        plt.scatter(x, y)
        plt.xlabel('{0} Rating'.format(cols[col]))
        plt.ylabel('Success Rate')

        plt.show()






if __name__ == '__main__':
    data = pd.read_csv('./dating.csv')
    visualize_gender(data=data)
    scatter_plots(data=data)
