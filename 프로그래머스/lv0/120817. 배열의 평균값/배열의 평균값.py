import numpy as np
def solution(numbers):
    arr = np.array(numbers)
    return np.mean(arr)
    # return sum(numbers)/len(numbers)