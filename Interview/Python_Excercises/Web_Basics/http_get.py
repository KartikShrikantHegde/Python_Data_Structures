import requests

# api-endpoint
URL = "https://jsonmock.hackerrank.com/api/movies/search/?"

# location given here
location = "spiderman"

# defining a params dict for the parameters to be sent to the API
params = {'Title': location, 'page':2}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=params)

# extracting data in json format
data = r.json()

print data

title = []


title.append(data['total'])
x  = data['data']
print x
print x[len(x)-1]['Title']