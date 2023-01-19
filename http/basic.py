# HTTP Verbs
# GET, POST, PUT, PATCH, DELETE

import requests

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers= { "Accept": 'application/json' })
# print(response.text)
# print(response.json())
data = response.json()
print(data['joke'])