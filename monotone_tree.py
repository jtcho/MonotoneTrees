import numpy as np

class MonotoneBinaryDecisionTree(object):
    """
    A simple implementation of a monotone binary decision tree,
    based on Potharst & Feelders' algorithm and ID3.
    """

    def fit(X_train, y):
        """
        Constructs and fits a monotone binary decision
        tree to the input dataset.

        :param X_train: an m x p nd-array of input features
        :param y: an m x 1 nd-array of class labels. It is further
        required that the dataset is:
        - consistent: x_i = x_j ==> y_i = y_j
        - monotone: x_i <= x_j ==> y_i <= y_j
        """
        raise NotImplementedError

    def predict(x):
        """
        Outputs a predictive class label for an input sample.

        :param x: a 1 x p nd-array representing a single input vector
        """
        raise NotImplementedError

