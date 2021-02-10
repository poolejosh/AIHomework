import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.lines import Line2D


def neural_network():
    # PART 1
    # get data from file and train neural network
    dataset = pd.read_excel("E:/AIProjects/homework3/HW3Data.xlsx")

    x = dataset.drop('Class', axis=1)
    y = dataset['Class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

    scaler = StandardScaler()
    scaler.fit(x_train)

    x_train_trans = scaler.transform(x_train)
    x_test_trans = scaler.transform(x_test)

    mlp = MLPClassifier(hidden_layer_sizes=(2,))
    mlp.fit(x_train_trans, y_train)

    # predict values for the training data
    predictions = mlp.predict(x_train_trans)

    # get untransformed data for comparison
    x_train_old = scaler.inverse_transform(x_train_trans)

    cmap = colors.ListedColormap(['k', 'r'])
    bounds = [0., 0.5, 1.]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    x_1 = []
    x_2 = []
    y_1 = []
    y_2 = []
    color_1 = []
    color_2 = []

    misclassified = 0
    # split up scatter points between same as actual and different than actual
    for i in range(predictions.size):
        if [x_train_old[i][0], x_train_old[i][1], predictions[i]] in dataset.values.tolist():
            x_1.append(x_train_old[i][0])
            y_1.append(x_train_old[i][1])
            color_1.append(predictions[i])
        else:
            x_2.append(x_train_old[i][0])
            y_2.append(x_train_old[i][1])
            color_2.append(predictions[i])
            misclassified += 1

    # plot scatter points
    fig, ax = plt.subplots()
    plt.ylim(bottom=0, top=69)
    plt.xlim(left=0, right=69)
    ax.scatter(x=x_1, y=y_1, c=color_1, cmap=cmap, norm=norm, marker='.')
    ax.scatter(x=x_2, y=y_2, c=color_2, cmap=cmap, norm=norm, marker='X')

    # create custom legend and put it on plot
    legend_elements = [Line2D([0], [0], marker='.', color='w', markerfacecolor='r', label='Class 1. Same as actual.'),
                       Line2D([0], [0], marker='.', color='w', markerfacecolor='k', label='Class 0. Same as actual.'),
                       Line2D([0], [0], marker='X', color='w', markerfacecolor='r', label='Class 1. Different than actual.'),
                       Line2D([0], [0], marker='X', color='w', markerfacecolor='k', label='Class 0. Different than actual.')]
    ax.legend(handles=legend_elements, loc='best')
    plt.savefig('plot_part_1.png')

    print(f'Misclassified points in part 1: {misclassified}')

    # PART 2
    # output confusion matrix and performance metrics using test data
    predictions = mlp.predict(x_test_trans)
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

    # PART 3
    # generate 70x70 grid
    n = []
    for i in range(70):
        for j in range(70):
            n.append([j, i])

    n_trans = scaler.transform(n)
    predictions = mlp.predict(n_trans)

    # put 1D predictions back into 2D array
    predictions_2d = []
    row = []
    i = 1
    for x in predictions:
        row.append(x)
        if i % 70 == 0:
            predictions_2d.append(row)
            row = []
        i += 1

    # plot predicted data
    plt.clf()
    fig, ax = plt.subplots()
    plt.ylim(bottom=0, top=69)
    plt.xlim(left=0, right=69)
    ax.imshow(predictions_2d, interpolation='none', cmap=cmap, norm=norm)
    plt.savefig('plot_part_3.png')

    # PART 4
    # use same data points as parts 1-3 with new hidden layer size
    mlp = MLPClassifier(hidden_layer_sizes=(6,))
    mlp.fit(x_train_trans, y_train)

    # predict values for the training data
    predictions = mlp.predict(x_train_trans)

    # get untransformed data for comparison
    x_train_old = scaler.inverse_transform(x_train_trans)

    cmap = colors.ListedColormap(['k', 'r'])
    bounds = [0., 0.5, 1.]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    x_1 = []
    x_2 = []
    y_1 = []
    y_2 = []
    color_1 = []
    color_2 = []

    misclassified = 0
    # split up scatter points between same as actual and different than actual
    for i in range(predictions.size):
        if [x_train_old[i][0], x_train_old[i][1], predictions[i]] in dataset.values.tolist():
            x_1.append(x_train_old[i][0])
            y_1.append(x_train_old[i][1])
            color_1.append(predictions[i])
        else:
            x_2.append(x_train_old[i][0])
            y_2.append(x_train_old[i][1])
            color_2.append(predictions[i])
            misclassified += 1

    # plot scatter points
    plt.clf()
    fig, ax = plt.subplots()
    plt.ylim(bottom=0, top=69)
    plt.xlim(left=0, right=69)
    ax.scatter(x=x_1, y=y_1, c=color_1, cmap=cmap, norm=norm, marker='.')
    ax.scatter(x=x_2, y=y_2, c=color_2, cmap=cmap, norm=norm, marker='X')

    # create custom legend and put it on plot
    legend_elements = [Line2D([0], [0], marker='.', color='w', markerfacecolor='r', label='Class 1. Same as actual.'),
                       Line2D([0], [0], marker='.', color='w', markerfacecolor='k', label='Class 0. Same as actual.'),
                       Line2D([0], [0], marker='X', color='w', markerfacecolor='r',
                              label='Class 1. Different than actual.'),
                       Line2D([0], [0], marker='X', color='w', markerfacecolor='k',
                              label='Class 0. Different than actual.')]
    ax.legend(handles=legend_elements, loc='best')
    plt.savefig('plot_part_4_1.png')
    print(f'Misclassified points in part 4: {misclassified}')

    # output confusion matrix and performance metrics using test data
    predictions = mlp.predict(x_test_trans)
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

    # predict class labels for 70x70 grid
    predictions = mlp.predict(n_trans)

    # put 1D predictions back into 2D array
    predictions_2d = []
    row = []
    i = 1
    for x in predictions:
        row.append(x)
        if i % 70 == 0:
            predictions_2d.append(row)
            row = []
        i += 1

    # plot predicted data
    plt.clf()
    fig, ax = plt.subplots()
    plt.ylim(bottom=0, top=69)
    plt.xlim(left=0, right=69)
    ax.imshow(predictions_2d, interpolation='none', cmap=cmap, norm=norm)
    plt.savefig('plot_part_4_2.png')


if __name__ == '__main__':
    neural_network()
