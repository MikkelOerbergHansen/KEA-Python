# import af modulet Flask
from flask import Flask, request, render_template, redirect, session
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt



def TreeExample():
    df = pandas.read_excel("Semester_2/SimCorp_stuff/Static/testData.xlsx", sheet_name="DecTree")

    d = {'UK': 0, 'USA': 1, 'N': 2}
    df['Nationality'] = df['Nationality'].map(d)
    d = {'YES': 1, 'NO': 0}
    df['Go'] = df['Go'].map(d)

    features = ['Age', 'Experience', 'Rank', 'Nationality']

    X = df[features]
    y = df['Go']

    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X, y)

    tree.plot_tree(dtree, feature_names=features)
    plt.savefig('Semester_2/SimCorp_stuff/Static//Treeplot.png')
    
    return df



data = TreeExample()
print(list(data["Age"])[0])
print(list(data["Experience"]))
print(list(data["Rank"]))
print(list(data["Nationality"]))
print(list(data["Go"]))

mydata = list(data)
print(mydata)