import requests
import pyfiglet
from random import choice

ascii_banner = pyfiglet.figlet_format("DAD JOKES", font="slant")
print(ascii_banner)

query = input("What joke would you like to search for : ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(url,
                        headers={"Accept": 'application/json'},
                        params={"term": query}
                        ).json()

num_jokes = response['total_jokes']
results = response['results']
if num_jokes > 1:
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(results[0]['joke'])
else:
    print(f"Sorry, no jokes found with search term {query}")
