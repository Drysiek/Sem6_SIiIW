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
    if std == 0:
        return 0.0
    p_x_given_y = (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-((feat_val-mean)**2 / (2 * std**2)))

    return p_x_given_y


def calculate_likelihood_categorical(df, feat_name, feat_val, label):
    df = df[df[10] == label]
    p_x_given_y = len(df[df[feat_name] == feat_val]) / len(df)
    return p_x_given_y


def get_max(post_prob, labels):
    maximum = post_prob[0]
    max_label = labels[0]
    for i in range(1, len(post_prob)):
        if post_prob[i] > maximum:
            maximum = post_prob[i]
            max_label = labels[i]
    return max_label


def naive_bayes_gaussian(df, x_test):
    features = list(range(1, 10))
    prior = calculate_prior(df)
    labels = sorted(list(df[10].unique()))

    y_predicted = []
    for index, x in x_test.iterrows():
        likelihood = [1.0]*len(labels)
        for j in range(len(labels)):
            for i in range(len(features)):
                likelihood[j] += calculate_likelihood_gaussian(df, features[i], x[i], labels[j])

        post_prob = [1]*len(labels)
        for j in range(len(labels)):
            post_prob[j] = likelihood[j] * prior[j]

        # y_predicted.append(get_max(post_prob, labels))
        y_predicted.append(np.argmin(post_prob))

    return np.array(y_predicted)


def naive_bayes_categorical(df, x_test):
    # get feature names
    features = list(df.columns)[:-1]

    # calculate prior
    prior = calculate_prior(df)

    y_predicted = []
    # loop over every data sample
    for index, x in x_test.iterrows():
        # calculate likelihood
        labels = sorted(list(df[10].unique()))
        likelihood = [0]*len(labels)
        for j in range(len(labels)):
            for i in range(len(features)):
                likelihood[j] += calculate_likelihood_categorical(df, features[i], x[i], labels[j])

        # calculate posterior probability (numerator only)
        post_prob = [1]*len(labels)
        for j in range(len(labels)):
            post_prob[j] = likelihood[j] * prior[j]

        y_predicted.append(get_max(post_prob, labels))

    return np.array(y_predicted)
