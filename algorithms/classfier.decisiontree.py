import pandas as pd
import numpy as np

from sklearn import datasets

def load_dataset():
    return datasets.load_iris()

    # return datasets.load_iris().data[:,:2], datasets.load_iris.target

# np.unique(datasets.load_iris().target)
# datasets.load_iris().feature_names[0:2]
# datasets.load_iris().data[:,:2]

# Util functions


def find_feature_cols(data):
    return data.feature_names[:2]

def find_unique_values(data, index=0):
    # This function will return array of unique values of a column in 1d or Nd array
    if data.ndim >1:
        return np.unique(data[:][index]) 
    
    return np.unique(data[:])

 
def question(arr,j):
    condition = arr <= j

    left_subtree = arr[condition]
    right_subtree = arr[~condition]

    return left_subtree, right_subtree

def gini(X, y):
    impurity = 1
    # class_tup_counts = np.unique(datasets.load_iris().target, return_counts=True)
    class_counts = {key : value for key, value in zip(list(np.unique(datasets.load_iris().target, return_counts=True)[0]),list(np.unique(datasets.load_iris().target, return_counts=True)[1]))}

    impurity = 1

    
    for key, value in class_counts.items():
        impurity -= (value/len(y))**2


    return impurity


def build_tree():
    # Extract data in Features and Target label
    data = load_dataset()
    X = data.data[:,:2]
    y = data.target

    impurity = gini(X,y)


    for i in range (len(find_feature_cols(data))):
        for j in find_unique_values(X, i):

            left_subtree, right_subtree = question(X[:][i])








    print('Checkpoint')
    # Find question to ask


build_tree()

# def question()