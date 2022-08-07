import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.array([1,2,3,np.nan,5,6,7,np.nan])



x = print(x[np.logical_not(np.isnan(x))])
