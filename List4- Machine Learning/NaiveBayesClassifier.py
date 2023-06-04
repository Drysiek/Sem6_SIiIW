import numpy as np


def calculate_prior(df):
    classes = sorted(list(df[10].unique()))
    prior = []
    for i in classes:
        prior.append(len(df[df[10] == i])/len(df))
    return prior


def calculate_likelihood_gaussian(df, feat_name, feat_val, label):
    df = df[df[10] == label]
    mean, std = df[feat_name].mean(), df[feat_name].std()
    p_x_given_y = (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-((feat_val-mean)**2 / (2 * std**2)))
    return p_x_given_y


def naive_bayes_gaussian(df, x_test):
    features = list(range(1, 10))
    prior = calculate_prior(df)

    y_predicted = []
    for index, x in x_test.iterrows():
        labels = [x for x in range(1, 8) if x != 4]
        likelihood = [1]*len(labels)
        for j in range(len(labels)):
            for i in range(len(features)):
                likelihood[j] *= calculate_likelihood_gaussian(df, features[i], x[i], labels[j])

        post_prob = [1]*len(labels)
        for j in range(len(labels)):
            post_prob[j] = likelihood[j] * prior[j]

        y_predicted.append(np.argmax(post_prob))

    return np.array(y_predicted)
