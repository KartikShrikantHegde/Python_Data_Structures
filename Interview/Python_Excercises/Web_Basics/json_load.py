# Json load allows us to load the response as json obj and then iteritate over it

import urllib.request
import json

from flask import request

with request.urlopen("https://www.google.com") as f:
    response = f.read

obj = json.load(response)
print obj['some-key']