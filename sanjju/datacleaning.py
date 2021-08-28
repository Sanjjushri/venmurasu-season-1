import os
import pandas as pd

df = pd.read_csv('../datasets/முதற்கனல்.csv')

intg =  ["1", "2", "3", "4", "5", "6","7", "8", "9", "0", "[", "]"]

for inte in intg:
    df['column1'] = df['column1'].str.replace(inte, ' ')