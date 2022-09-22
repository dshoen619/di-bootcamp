import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import seaborn as sns
import matplotlib as mpl

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# ax=sns.boxplot(x="Sex", y="Age", data=df)

# plt.show()

# ax1=sns.load_dataset(df)
# f, ax = plt.subplots(figsize=(6.5, 6.5))
# ax1=sns.despine(f, left=True, bottom=True)

# sns.scatterplot(x="Age", y="Fare",

#                 palette="ch:r=-.2,d=.3_r",

#                 sizes=(1, 8), linewidth=0,
#                 data=df, ax=ax)
# plt.show()

sns.set_theme(style="ticks")
f, ax = plt.subplots(figsize=(7, 5))
sns.despine(f)
sns.histplot(
    df,
    x="Age", hue="Fare",
    multiple="stack",
    palette="light:m_r",
    edgecolor=".3",
    linewidth=.5,
    log_scale=True,
)
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())

plt.show()


