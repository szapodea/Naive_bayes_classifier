import Bin
import pandas as pd
import numpy as np



class NBC:
    def __init__(self, t_frac, laplace=1):
        self.t_frac = t_frac
        self.laplace = laplace


    def nbc(self, t_frac):
        binned_data = pd.read_csv('./dating-binned.csv')
        binned_data.drop('Unnamed: 0', axis = 1, inplace=True)
        data = pd.read_csv('./trainingSet.csv')
        data.drop('Unnamed: 0', axis=1, inplace=True)
        trainingData = data.sample(random_state=47, frac=t_frac)
        class_probs = self.classProbs(trainingData)

        probs_dict = self.getLabelProbs(training_data=trainingData, class_probs=class_probs, overall_data=binned_data)
        percentage = self.predict_decisions(data=trainingData, probs=probs_dict, class_probs=class_probs)
        print(percentage)
        testData = pd.read_csv('./testSet.csv')
        testData.drop('Unnamed: 0', axis=1, inplace=True)
        testingData = testData.sample(random_state=47, frac=t_frac)
        percentage = self.predict_decisions(data=testingData, probs=probs_dict, class_probs=class_probs)
        print(percentage)
    def classProbs(self, trainingData):
        class_probs = {}
        for val in trainingData['decision']:
            if val not in class_probs:
                class_probs[val] = 1
            else:
                class_probs[val] += 1

        class_probs[0] = class_probs[0] / (class_probs[0] + class_probs[1])
        class_probs[1] = 1 - class_probs[0]
        print(class_probs)
        return class_probs


    def getLabelProbs(self, training_data, class_probs, overall_data):
        decision_data = training_data['decision']
        probs = {}
        #probs['age'] = self.labelProb(label_data=training_data['age'], class_probs=decision_data, overall_data=overall_data['age'])

        for col in list(training_data.columns):
            probs[col] = self.labelProb(label_data=training_data[col], class_probs=decision_data, overall_data=overall_data[col])

        return probs


    def labelProb(self, label_data, class_probs, overall_data):
        label_prob = {}
        # Look at the entire dataset for every possible label
        for val in overall_data:
            if val not in label_prob:
                label_prob[val] = 0

        probs = {}
        for val in label_prob:
            for cat in set(class_probs):
                val_count = 0
                cat_count = 0
                for i, j in zip(label_data, class_probs):
                    if i == val and j == cat:
                        val_count += 1
                    if j == cat:
                        cat_count += 1
                # Smoothing
                probs[(val, cat)] = (val_count + self.laplace)/(cat_count + (len(label_prob) * self.laplace))
        return probs


    def predict_decisions(self, data, probs, class_probs):
        correct, total = 0, 0
        for index, row in data.iterrows():
            one_prob = class_probs[0]
            zero_prob = class_probs[1]
            for col in data.columns:
                one_prob *= probs[col][(row[col], 1)]
                zero_prob *= probs[col][(row[col], 0)]

            if one_prob > zero_prob:
                if row['decision'] == 1:
                    correct += 1
            elif one_prob < zero_prob:
                if row['decision'] == 0:
                    correct += 1
            else:
                correct += 1

            total += 1
        print(correct, total)
        return correct / total













if __name__ == '__main__':
    bins = [2, 5, 10, 50, 100, 200]
    data = pd.read_csv('./dating.csv')
    for bin in bins:
        Bin.into_bins(data=data, bins = bin, file_name='./dating-binned-2.csv')
        data_binned = pd.read_csv('./dating-binned-2.csv')
        Bin.split(data=data_binned, test_file='./testSet-binned.csv', training_file='./trainingSet-binned.csv')


    classifier = NBC(t_frac=1, laplace=1)
    classifier.nbc(t_frac=classifier.t_frac)