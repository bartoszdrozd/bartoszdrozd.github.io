import pandas as pd
import plotly.express as px

url ='http://api.open-notify.org/iss-now.json'

df = pd.read_json(url)
df = df.drop(['message'], axis=1)
df = df.drop(['timestamp'], axis=1)

print(df.transpose())

fig = px.scatter_geo(df, lat=['latitude'], lon=['longitude'])
fig.show()