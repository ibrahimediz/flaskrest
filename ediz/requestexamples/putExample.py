import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {'userId': 1, 'title': 'İKİ EKMEK', 'completed': False}
response = requests.put(api_url,json=todo)
print(response.json())
print(response.status_code)


response = requests.get(api_url)
print(response.json())