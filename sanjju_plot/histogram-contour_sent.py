import plotly.express as px
import pandas as pd

df = pd.read_csv('../datasets/முதற்கனல்_2.csv')

fig = px.density_contour(df, x="column1", y="wordCount", title='Lenght of each sentence in முதற்கனல்')
fig.update_traces(contours_coloring="fill", contours_showlabels = True)
fig.show()