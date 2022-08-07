import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import datetime

N= random.randint(1,40)
M= random.randint(1,50)

array=[]
for i in range(N):
    list_content=[]
    for i in range(M):
        list_content.append(random.randint(1,100))
    array.append(list_content)

# print(array[2])

# for i in array:
#     print(i[2])

# for i in array[len(array)-1]:
#     i==0

sum_first_two=0
for i in array:
    sum_first_two+=i[0]+i[1]

for i in array:
    i[len(array)-1]==sum_first_two


numpy_list= np.random.randint(100,size=(M,N))
# print(numpy_list[2])

numpy_list[N]=0



