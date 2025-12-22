from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

xpoints = np.array([1,2,3,4,5]) #Time
ypoints = np.array([5,7,2,4,3]) #Price


url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
  'id': 1,
  'convert':'CAD'
}

api_key = os.getenv("PRO_API_KEY")
if not api_key:
    raise RuntimeError("Missing PRO_API_KEY")

headers = {
    "Accept": "application/json",
    "X-CMC_PRO_API_KEY": api_key
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    price = data['data']['1']['quote']['CAD']['price']
    print(data)
    print(price)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
    
    
plt.plot(xpoints, ypoints, marker = 'o', linestyle = '-', color='b')

plt.title("BTC Price Over Time")
plt.xlabel("Current Time") 
plt.ylabel("Price per 1 BTC") 
plt.show()  