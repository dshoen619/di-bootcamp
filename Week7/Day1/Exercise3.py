import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random


random_array=np.random.randint(100,size=(5,6))

print(random_array)

for i in random_array:
    print(max(i))