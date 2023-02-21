import pandas as pd
import numpy as np

from sklearn import datasets

def load_dataset():
    return datasets.load_iris().data[:,:2], datasets.load_iris.target

class Node():
    def __init__(self,left = None, right = None, threshold = None, feature_index = None,
                    information_gain = None, value = None):

        """
        This constructor method to initialize properties of Node of Binary Tree
        
        There will be two type of Nodes; 
        1. Decision Node
        2. Leaf Node
        """

        # Decision Node
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.information_gain = information_gain

        # Leaf Node: Value of majority class
        self.value = value      
       


class Tree():
    """This class is responsible for creating Binary Decision Tree 
    """

    def __init__(self, max_depth = 2, min_sample_split = 2):
        """
        This constructor will initialize 
        """
        self.root = None


        self.max_depth = max_depth
        self.min_sample_split = min_sample_split


    
    def build_tree(self, data, curr_depth):
        print('Hello')


load_dataset()