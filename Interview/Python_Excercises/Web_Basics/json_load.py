# Json load allows us to load the response as json obj and then iteritate over it

import urllib.request
import json

with urllib.request.urlopen("https://www.google.com") as f:
    response = f.read

obj = json.load(response)
print obj['some-key']