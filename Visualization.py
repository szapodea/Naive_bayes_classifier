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








if __name__ == '__main__':
    data = pd.read_csv('./dating.csv')
    visualize_gender(data=data)