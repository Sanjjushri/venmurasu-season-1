import plotly.express as px
import pandas as pd

df = pd.read_csv('../datasets/முதற்கனல்_2.csv')

fig = px.scatter(df, x = 'column1', y = 'wordCount', title='Count of how many times the Word is used in முதற்கனல்')
fig.show()