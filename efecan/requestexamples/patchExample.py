import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

todo = {'title': 'Emanet alcan aslanım'}
response = requests.patch(apiurl,json=todo)
print(response.json())
print(response.status_code)
