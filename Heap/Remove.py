import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
}

r = requests.post(
    'http://taxee.io/api/v1/calculate/2014',
    data=data,
    headers=headers
)

print(r.text)