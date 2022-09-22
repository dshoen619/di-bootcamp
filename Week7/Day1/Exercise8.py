import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import datetime

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

df2.rename(columns={'pazham':'fruit', 'kilo':'weight'}, inplace=True)

frames=[df1,df2]

print(pd.concat(frames))






