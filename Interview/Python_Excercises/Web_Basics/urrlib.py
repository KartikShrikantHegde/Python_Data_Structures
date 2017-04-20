# urllib2 is a Python module for to access web pages or other resources over the network

# It can act like HTTP get request.

# It gets the response which is similer to a file like object -> we can call read or readline on it.


import urllib.request

with urllib.request.urlopen("https://www.google.com") as f:
    response = f.read