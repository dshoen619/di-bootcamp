import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import datetime

names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)

print(df_mpg)
