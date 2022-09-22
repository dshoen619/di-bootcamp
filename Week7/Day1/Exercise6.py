import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import datetime

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# print(df.info())



df.rename(columns={'Type':'TypeOfCar'}, inplace=True)

# print(df.head())

print(df.isna().sum())
print(max(df.isna().sum()))





