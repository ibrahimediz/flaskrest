import requests

api_url = apiurl = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print(response.json())

todo = {'userid':1, 'title': "iki ekmek", 'completed': False}
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)

response = requests.get(api_url)
print(response.json())