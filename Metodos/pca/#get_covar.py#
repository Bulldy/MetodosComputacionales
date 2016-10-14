# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:09:03 2016

@author: juan
"""

import numpy as np

names = ['data_A.txt', 'data_B.txt', 'data_C.txt']      # names of files to load

data = [np.genfromtxt(name) for name in names]      # loaded data

def E(values):
    """
        Returns the expected value of a variable based on its values
    """
    
    return sum(values)/len(values)


def cov(data_array):    
    """
        Returns covariance matrix of the data in data_array
    """    
    
    number = len(data_array[0])         # number of variables
    cov_matrix = np.ones((number, number))      # square matrix
    
    for i in range(number):
        for j in range(number):
            data_1 = data_array[:, i]       # variable 1
            data_2 = data_array[:, j]       # variable 2
            
            mu_1 = E(data_1)        # expected value of variable 1
            mu_2 = E(data_2)        # expected value of variable 2
            
            expectant = E((data_1 - mu_1) * (data_2 - mu_2))        # covariance between variable 1 and 2
            cov_matrix[i, j] = expectant        # includes result to the matrix
            
    return cov_matrix
    
for item in data:
    result = cov(item)
    print(result)