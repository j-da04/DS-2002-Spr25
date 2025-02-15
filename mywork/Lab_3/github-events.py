#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
import os
import json
import requests

#GHUSER = os.getenv('j-da04')
GHUSER = "j-da04"

url = 'https://api.github.com/users/{0}/events'.format(GHUSER)

print(url)
print(GHUSER)

r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)

