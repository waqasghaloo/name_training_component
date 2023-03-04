import pandas as pd
import numpy as np

from sklearn import datasets


class Decision_Node:
    """Decision node asks a question
        This holds reference to question, left_branch and right_branch
    """

    def __init__(self,question, left_branch, right_branch):
        self.question = question
        self.left_branch = left_branch
        self.right_branch = right_branch


def load_dataset():
    # returns 2d array with 2 features and 1 target column
    return np.c_[ datasets.load_iris().data[:,:2], datasets.load_iris().target ]  

    # return datasets.load_iris().data[:,:2], datasets.load_iris.target

# np.unique(datasets.load_iris().target)
# datasets.load_iris().feature_names[0:2]
# datasets.load_iris().data[:,:2]

# Util functions


def find_feature_cols(data):
    return data.feature_names

def find_unique_values(data, index=0):
    # This function will return array of unique values of a column in 1d or Nd array
    if data.ndim >1:
        print('Nd')
        return np.unique(data[:,index]) 
    
    return np.unique(data[:])

 
def question(arr,i,j):
    condition = arr[:,i] <= j

    left_subtree = arr[condition]
    right_subtree = arr[~condition]

    return left_subtree, right_subtree

def gini(data):



    impurity = 1
    # class_tup_counts = np.unique(datasets.load_iris().target, return_counts=True)
    class_counts = {key : value for key, value in zip(list(np.unique(data[:,-1], return_counts=True)[0]),list(np.unique(data[:,-1], return_counts=True)[1]))}

    # impurity = 1

    
    for key, value in class_counts.items():
        impurity -= (value/len(data[:,-1]))**2


    return impurity


def info_gain(left_subtree, right_subtree, impurity):
    # Information Gain uses classes weightage and Entropy/Gini to calculate impurity at node
    # Information Gain tells how much impurity is being reduced 
    
    size = len(left_subtree) + len(right_subtree)
    ig = impurity - (len(left_subtree)/size) *gini(left_subtree) - (len(right_subtree)/size) *gini(right_subtree)

    return ig

def best_split(data):
    # Extract data in Features and Target label
    
    best_gain = 0
    best_question = None

    split_value = 0
    left_branch = None
    right_branch = None

    # X = data.data
    # y = data.target

    impurity = gini(data)


    for i in range (data[:,:-1].ndim):
        for j in find_unique_values(data[:,:-1], i):

            # impurity = gini(X,y)

            left_subtree, right_subtree = question(data,i,j)

            if len(left_subtree) == 0 or len(right_subtree) == 0:
                continue

            
            gain = info_gain(left_subtree, right_subtree, impurity)

            if gain>=best_gain:
                print(gain)
                best_gain = gain
                best_question = i
                split_value = j
                left_branch = left_subtree
                right_branch = right_subtree

    
                
                


    return best_gain, best_question, left_branch, right_branch


def build_tree(data):
    best_gain, best_question, left_branch, right_branch = best_split(data)
    print(best_question, best_gain)

    if best_gain == 0:
        print('Calling Leaf function')

    build_tree(left_branch)
    build_tree(right_branch)

    return Decision_Node(question, left_branch, right_branch)



data = load_dataset()

node = build_tree(data)



