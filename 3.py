import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv", sep=";", header=None)
df.columns = ['prep', 'group', 'marks']
gr1 = df.groupby(['prep', 'marks'])['prep'].count().unstack('marks').fillna(0)
gr2 = df.groupby(['group', 'marks'])['group'].count().unstack('marks').fillna(0)
ax = gr1.plot(kind='bar', stacked=True, rot=0)
plt.savefig('preps.png')
bx = gr2.plot(kind='bar', stacked=True, rot=0)
plt.savefig('groups.png')
plt.show()
