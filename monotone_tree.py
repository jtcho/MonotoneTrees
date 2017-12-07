import numpy as np

class MonotoneBinaryDecisionTree(object):
    """
    A simple implementation of a monotone binary decision tree
    for discrete input spaces, based on Potharst & Feelders'
    algorithm and ID3.
    """

    def _validate_monotonicity(self, X, y):
        """
        Validates whether the given input dataset
        is in fact monotone.
        """
        raise NotImplementedError

    def _tree(self, X_train, y):
        raise NotImplementedError

    def _split(self, X, y):
        raise NotImplementedError

    def fit(self, X_train, y):
        """
        Constructs and fits a monotone binary decision
        tree to the input dataset.

        :param X_train: an m x p nd-array of input features.
        It is further required that the attributes are discrete,
        represented as integers (the mapping should be handled
        externally).
        :param y: an m x 1 nd-array of class labels.
        It is further required that the dataset is:
        - consistent: x_i = x_j ==> y_i = y_j
        - monotone: x_i <= x_j ==> y_i <= y_j
        """
        raise NotImplementedError

    def predict(self, x):
        """
        Outputs a predictive class label for an input sample.

        :param x: a 1 x p nd-array representing a single input vector
        """
        raise NotImplementedError

