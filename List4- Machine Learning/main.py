import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import os
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error


def get_data():
    file = 'glass.data'
    data_frame = pd.read_csv(file, sep=',', header=None)
    # print(data_frame)
    return data_frame


def get_stats(data_frame):
    description = ["data_frame[0]: //row ID",
                   "\ndata_frame[1]: //glass refractive index- współczynnik załamania szkła",
                   "\ndata_frame[2]: //Na- weight percent in sodium oxide",
                   "\ndata_frame[3]: //Mg- weight percent in magnesium oxide",
                   "\ndata_frame[4]: //Al- weight percent in aluminium oxide",
                   "\ndata_frame[5]: //Si- weight percent in silicon oxide",
                   "\ndata_frame[6]: //K- weight percent in potassium oxide",
                   "\ndata_frame[7]: //Ca- weight percent in calcium oxide",
                   "\ndata_frame[8]: //Ba- weight percent in barium oxide",
                   "\ndata_frame[9]: //Fe- weight percent in iron oxide",
                   "\ndata_frame[10]: //type of glass"]

    for i in range(0, 11):
        print(description[i])
        print(data_frame[i].unique())
        print("Number of unique values", len(data_frame[i].unique()))
        print("Max value", data_frame[i].unique().max())
        print("Min value", data_frame[i].unique().min())


def get_cross_validation(data_frame, answers):
    x_train, x_test, y_train, y_test = train_test_split(data_frame, answers, test_size=.20, random_state=40)

    # cv_temp_glass_type = data_frame.groupby(df[10])
    # cv_glass_type = []
    # for i in temp_glass_type:
    #     glass_type.append(i[1])
    # pass

    return x_train, x_test, y_train, y_test


def discretization(data_frame, precision=10, starting_position=4):
    discretized_data = data_frame.copy()
    for i in range(1, 10):
        _, bins = pd.qcut(data_frame[i], q=precision, retbins=True, labels=False, duplicates='drop')
        labels = list(range(starting_position, starting_position + len(bins) - 1))
        discretized_data[i] = pd.cut(data_frame[i], bins=bins, labels=labels, include_lowest=True)
    return discretized_data


def normalization(data_frame):
    normalized_data = data_frame.copy()
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(normalized_data)
    return normalized_data


def standardization(data_frame):
    standardized_data = data_frame.copy()
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(standardized_data)
    return standardized_data


if __name__ == '__main__':
    df = get_data()
    # get_stats(df)

    temp_glass_type = df.groupby(df[10])
    glass_type = []
    temp_iterator = 0
    for i in temp_glass_type:
        glass_type.append(i[1])
        temp_iterator += 1
        # get_stats(glass_type[temp_iterator])
        # print('---------------------------------------\n')

    y = df[10]
    x = df.drop([10], axis=1)

    x_train, x_test, y_train, y_test = get_cross_validation(x, y)

    # discretized_glass_data = discretization(x, 5, 4)
    # normalized_glass_data = normalization(x)
    # standardized_glass_data = standardization(x)
