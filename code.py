import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")
mean = df.groupby(['student_id', 'level'], as_index=False)['attempt'].mean()


# fig = go.Figure(go.Bar(
#   x=df.groupby('level')['attempt'].mean(),
#   y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
#   orientation='h'
# ))

# fig.show()

fig = px.scatter(mean, x="student_id", y="level", size='attempt', color='attempt')
fig.show()