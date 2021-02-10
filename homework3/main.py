import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
import graphviz
import matplotlib.pyplot as plt
from matplotlib import colors


def decision_tree():
    # PART 1
    dataset = pd.read_excel("E:/AIProjects/homework3/HW3Data.xlsx")

    x = dataset.drop('Class', axis=1)
    y = dataset['Class']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(x_train, y_train)

    tree.plot_tree(classifier)

    dot_data = tree.export_graphviz(classifier, out_file=None)
    graph = graphviz.Source(dot_data)
    graph.render("tree")

    # PART 2
    y_pred = classifier.predict(x_test)
    print("Confusion matrix:")
    print(metrics.confusion_matrix(y_test, y_pred))
    print("Performance metrics:")
    print(metrics.classification_report(y_test, y_pred))

    # PART 3
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(x, y)
    tree.plot_tree(classifier)

    dot_data = tree.export_graphviz(classifier, out_file=None)
    graph = graphviz.Source(dot_data)
    graph.render("tree_2")

    n = []
    for i in range(70):
        for j in range(70):
            n.append([i, j])

    y_pred_70 = classifier.predict(n)
    y_pred_70_2d = []
    row = []
    i = 1
    for x in y_pred_70:
        row.append(x)
        if i % 70 == 0:
            y_pred_70_2d.append(row)
            row = []
        i += 1

    fig, ax = plt.subplots()
    cmap = colors.ListedColormap(['k', 'r'])
    bounds = [0., 0.5, 1.]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.ylim(bottom=0, top=69)
    plt.xlim(left=0, right=69)
    ax.imshow(y_pred_70_2d, interpolation='none', cmap=cmap, norm=norm)
    plt.savefig('plot.png')

    # PART 4
    plt.clf()
    plt.ylim(bottom=0, top=69)
    plt.xlim(left=0, right=69)
    for value in dataset.values:
        x = value[0]
        y = value[1]
        if value[2] == 1:
            color = 'red'
        else:
            color = 'black'
        plt.scatter(x=x, y=y, color=color)
    plt.savefig('plot_2.png')


if __name__ == '__main__':
    decision_tree()
