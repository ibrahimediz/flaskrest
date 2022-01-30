import requests, json

apiurl = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(apiurl)

response = requests.get(apiurl)
print(response.json())

response = requests.delete(apiurl)
print(response.json())
print(response.status_code)