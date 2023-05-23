import requests

BaseURL = "https://petstore.swagger.io/v2"

#Get запросы
username = 'user1'

res = requests.get( f"{BaseURL}/user/{username}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.text)


status = 'available'

res = requests.get( f"{BaseURL}/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.json())

#POST запрос
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

#DELETE запрос
headers = {
    'accept': 'application/json',
   }

response = requests.delete(f"{BaseURL}/user/Pop", headers = headers)

print(response.status_code)
print(response.text)

#PUT запрос
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
