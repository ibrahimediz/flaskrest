import requests
api_url = "https://jsonplaceholder.typicode.com/todos/19"
response = requests.get(api_url)
print(response.json())


response = requests.delete(api_url)
print(response.json())
print(response.status_code)