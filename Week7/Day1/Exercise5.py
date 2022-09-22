import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import datetime

series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])

for i in series:
    date=(pd.to_datetime(i))
    print(date.day_of_month)
    print(date.day_of_year)
    print(date.day_of_week)
    print(date.week)
    print(date.month)




