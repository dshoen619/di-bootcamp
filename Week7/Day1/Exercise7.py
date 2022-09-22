import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import datetime

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df.drop('EngineSize', axis=1,inplace=True)

del df['Length']

print(df.head())







