import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    number_list = []
    for i in range (len(L)):
        soft_max = np.e**L[i]/sum(np.exp(L))
        number_list.append(soft_max)
    return number_list
