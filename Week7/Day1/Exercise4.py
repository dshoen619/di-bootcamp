import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random


series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))



unique_letters= series.unique()
unique_letters_dict={}
for i in unique_letters:
    unique_letters_dict[i]=0


for i in series:
    unique_letters_dict[i]+=1

print(unique_letters_dict)