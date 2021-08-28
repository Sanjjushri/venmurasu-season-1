import pandas as pd
import plotly.express as px

df = pd.read_csv('../datasets/முதற்கனல்_4.csv')

fig = px.line(df, x = 'word', y = 'count', title='Count of how many times the Word is used in முதற்கனல்')
fig.show()