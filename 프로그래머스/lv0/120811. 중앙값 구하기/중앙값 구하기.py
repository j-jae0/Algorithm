# import pandas as pd
# import numpy as np

# def solution(array):
#     arr = pd.Series(array) 
#     return arr.median()

def solution(array):
    s_arr = sorted(array)
    print(s_arr)
    if len(s_arr)%2 == 0:
        return int((s_arr[len(s_arr)//2] + s_arr[(len(s_arr)-1)//2])/2)
    else:
        return s_arr[len(s_arr)//2]