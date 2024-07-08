import requests

import json

 

url = "http://127.0.0.1:5000/api/get"

 

payload = json.dumps({"address": "D300"})

headers = {

  'Content-Type': 'application/json'

}

requests.packages.urllib3.disable_warnings()

#response = requests.request("POST", url, headers=headers, data=payload)

response = requests.request("POST", url, headers=headers, data=payload,verify=False)

print(response.text)

 

url = "http://127.0.0.1:5000/api/put"

 

payload = json.dumps({"address": "D300", "value": 1})

headers = {

  'Content-Type': 'application/json'

}

requests.packages.urllib3.disable_warnings()

#response = requests.request("POST", url, headers=headers, data=payload)

response = requests.request("POST", url, headers=headers, data=payload,verify=False)

print(response.text)

 

 

url = "http://127.0.0.1:5000/api/get"

 

payload = json.dumps({"address": "D300"})

headers = {

  'Content-Type': 'application/json'

}

requests.packages.urllib3.disable_warnings()

#response = requests.request("POST", url, headers=headers, data=payload)

response = requests.request("POST", url, headers=headers, data=payload,verify=False)

print(response.text)