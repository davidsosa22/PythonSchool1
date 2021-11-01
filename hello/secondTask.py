import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import requests

# 3. Using Python and the Requests library write a 'get' request to pull the streetlights data. There is an API link on the dataset export tab.
# use try except block
try:
    api_endpoint = "https://data.nola.gov/resource/f3em-yyvw.json"
    receive = requests.get(api_endpoint)
    receive.json()
    receive.raise_for_status()
    print("Success")
except requests.exceptions.HTTPError as e:
    print (e.response.text)
# print(receive.text)

# 4. Using Python and the Pandas library, read the streetlights json data into a dataframe.
data = receive.text
df = pd.read_json(data)
# print(df)

# 5. Using Python, the Pandas histogram function, and Matplotlib plot a histogram of the streetlight Suport Arm Type column. Save the histogram as Figure_1.png and attach with submission.
# datafile = data
# fig = plt.figure(figsize=(16,6))
# plt.hist(df.supparmtyp)

_, _, patches = plt.hist(df.supparmtyp, align="mid")

# iterate over patches to get the exact value to show
for pp in patches:
   x = (pp._x0 + pp._x1)/2
   y = pp._y1 + 0.05
   plt.text(x, y, pp._y1)
plt.title('Histogram of Suport Arm Type ', loc = 'left', fontsize = 18)
plt.show()