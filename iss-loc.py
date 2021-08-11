import pandas as pd

url ='http://api.open-notify.org/iss-now.json'

df = pd.read_json(url)
latitude = df['iss_position']['latitude']
longitude = df['iss_position']['longitude']
print(latitude, longitude)