import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_numpy_array(start,length,step):
    reg_array=[]
    i=0
    while i<length:
        if i==0:
            reg_array.append(start)
        else:
            start+=step
            reg_array.append(start)
        i+=1
    numpy_arr=np.array(reg_array)
    return numpy_arr

print(create_numpy_array(2,10,2))


