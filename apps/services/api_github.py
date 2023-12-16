import requests
from pprint import pprint

url = "https://api.github.com/users/ratarov"
r = requests.get(url=url)
resp = r.json()
pprint(resp)
