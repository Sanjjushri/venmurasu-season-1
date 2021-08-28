import plotly.express as px
import pandas as pd

df = pd.read_csv('../datasets/முதற்கனல்_4.csv')

fig = px.density_contour(df, x="count", y="word", title='Count of how many times the Word is used in முதற்கனல்')
fig.update_traces(contours_coloring="fill", contours_showlabels = True)
fig.show()