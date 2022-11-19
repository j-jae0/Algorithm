import pandas as pd
import numpy as np

def solution(array):
    
    arr = pd.Series(array)
    
    return arr.median()