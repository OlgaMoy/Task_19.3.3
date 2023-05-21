import requests

BaseURL = "https://petstore.swagger.io/v2"
username = 'user1'

res = res = requests.get( f"{BaseURL}/user/{username}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.text)

status = 'available'

res = res = requests.get( f"{BaseURL}/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.json())


headers = {'accept': 'application/json',
           'ContentType': 'application/json'}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Baddy",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.post(f"{BaseURL}/pet", headers = headers, json = data)

print(res.status_code)
print(res.json())


url = 'https://petstore.swagger.io/v2/user/Pop)'

headers = {
    'accept': 'application/json',
   }

response = requests.delete(url, headers = headers)

print(response.status_code)
print(response.text)

headers = {'accept': 'application/json',
           'ContentType': 'application/json'}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res = requests.put(f"{BaseURL}/pet", headers = headers, json = data)

print(res.status_code)
print(res.json())
