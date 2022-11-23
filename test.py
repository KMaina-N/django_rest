import requests

import requests

url = "http://localhost:8000/api/students/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
