
import numpy as np
import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns

df = pd.read_csv('../datasets/முதற்கனல்.csv')

# # #df.info()

# # print(sns.heatmap(df.isnull(), cbar=False))

import missingno as msno
msno.matrix(df)

df.isna().sum()

a=msno.matrix(df)

print(a)


