import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from NaiveBayesClassifier import naive_bayes_gaussian, naive_bayes_categorical
from matplotlib import pyplot as plt


test_size = .2
reach = range(0, int(214 * test_size))


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


def get_correlation_heatmap(data_frame):
    import seaborn as sns
    import matplotlib.pyplot as plt

    corr = data_frame.iloc[:, 1:-1].corr(method="pearson")
    cmap = sns.diverging_palette(250, 354, 80, 60, center='dark', as_cmap=True)

    plt.figure(figsize=(10, 8))  # Set the size of the figure
    sns.heatmap(corr, vmax=1, vmin=-.5, cmap=cmap, square=True, linewidths=.2)

    plt.title("Correlation Heatmap")  # Set the title of the plot
    plt.show()


def push_4_to_data(data_frame):
    data_frame[10] = data_frame[10].replace({7: 4})
    return data_frame


def discretization(data_frame, precision=10, starting_position=4):
    discretized_data = data_frame.copy()
    for i in range(1, 10):
        _, bins = pd.qcut(data_frame[i], precision=2, q=precision, retbins=True, labels=False, duplicates='drop')
        labels = list(range(starting_position, starting_position + len(bins) - 1))
        discretized_data[i] = pd.cut(data_frame[i], bins=bins, labels=labels, include_lowest=True)
        discretized_data = discretized_data.astype(float)
    return discretized_data


def normalization(data_frame):
    normalized_data = data_frame.copy()
    scaler = MinMaxScaler()

    first_column = normalized_data.iloc[:, 0]
    last_column = normalized_data.iloc[:, -1]

    normalized_data.iloc[:, 1:-1] = scaler.fit_transform(normalized_data.iloc[:, 1:-1])

    normalized_data.iloc[:, 0] = first_column
    normalized_data.iloc[:, -1] = last_column

    return normalized_data


def standardization(data_frame):
    standardized_data = data_frame.copy()
    scaler = StandardScaler()

    first_column = standardized_data.iloc[:, 0]
    last_column = standardized_data.iloc[:, -1]

    standardized_data.iloc[:, 1:-1] = scaler.fit_transform(standardized_data.iloc[:, 1:-1])

    standardized_data.iloc[:, 0] = first_column
    standardized_data.iloc[:, -1] = last_column
    return standardized_data


def compare(y_predicted, y_true):
    correctly_predicted = 0
    for i, j in zip(y_predicted, y_true):
        # print(i, j)
        if j == i:
            correctly_predicted += 1
    return correctly_predicted, len(y_true)


def show_naive_bayes(train, x_test, y_test, text, color):
    y_predicted = naive_bayes_gaussian(train, x_test)
    print(text, ' gaussian method:\t', compare(y_predicted, y_test))
    y_predicted = naive_bayes_categorical(train, x_test)
    print(text, 'categorical method:\t', compare(y_predicted, y_test))

    # print(len(reach))
    # print(len(y_predicted))

    plt.scatter(range(len(y_predicted)), y_predicted, color=color, marker='x')


def execute_naive_bayes(data_frame):
    discretized_glass_data = discretization(data_frame, 10, 4)
    normalized_glass_data = normalization(data_frame)
    standardized_glass_data = standardization(data_frame)

    # print(discretized_glass_data, '\n')
    # print(normalized_glass_data, '\n')
    # print(standardized_glass_data, '\n')

    df_concat = pd.concat([data_frame, discretized_glass_data, normalized_glass_data, standardized_glass_data], axis=1)
    train, test = train_test_split(df_concat, test_size=test_size, random_state=40)

    # Split the train set into individual DataFrames
    train_data_frame = train.iloc[:, 0:11]
    train_discretized_glass_data = train.iloc[:, 11:22]
    train_normalized_glass_data = train.iloc[:, 22:33]
    train_standardized_glass_data = train.iloc[:, 33:44]

    # Split the test set into individual DataFrames
    test_data_frame = test.iloc[:, 0:11]
    x_test_normal = test_data_frame.drop([10], axis=1)
    y_test_normal = test_data_frame[10]
    test_discretized_glass_data = test.iloc[:, 11:22]
    x_test_discretized = test_discretized_glass_data.drop([10], axis=1)
    y_test_discretized = test_discretized_glass_data[10]
    test_normalized_glass_data = test.iloc[:, 22:33]
    x_test_normalized = test_normalized_glass_data.drop([10], axis=1)
    y_test_normalized = test_normalized_glass_data[10]
    # test_standardized_glass_data = test.iloc[:, 33:44]
    # x_test_standardized = test_standardized_glass_data.drop([10], axis=1)
    # y_test_standardized = test_standardized_glass_data[10]

    # (train, x_test, y_test, text)
    show_naive_bayes(train_data_frame, x_test_normal, y_test_normal, 'normal data', 'red')
    show_naive_bayes(train_discretized_glass_data, x_test_discretized, y_test_discretized, 'discretized data', 'magenta')
    show_naive_bayes(train_normalized_glass_data, x_test_normalized, y_test_normalized, 'normalised', 'blue')
    # show_naive_bayes(train_standardized_glass_data, x_test_standardized, y_test_standardized, 'standardized', 'cyan')

    plt.title('Custom model regression')
    plt.xlabel("Test number")
    plt.ylabel("Number of fish")
    # plt.scatter(range(len(y_test_normal)), y_test_normal, color='green')

    plt.show()


if __name__ == '__main__':
    df = get_data()

    # get_stats(df)
    # get_correlation_heatmap(df)

    df = push_4_to_data(df)
    # print(df)

    temp_glass_type = df.groupby(df[10])
    glass_type = []
    temp_iterator = 0
    for i in temp_glass_type:
        glass_type.append(i[1])
        # get_stats(glass_type[temp_iterator])
        # print('---------------------------------------\n')
        temp_iterator += 1

    execute_naive_bayes(df)
