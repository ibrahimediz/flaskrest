import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())

response = requests.delete(api_url)
print(response.json())
print(response.status_code)
response2 = requests.delete(api_url)
print(response2.status_code)