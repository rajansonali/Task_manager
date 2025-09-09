import requests

url = "http://127.0.0.1:5000/api/tasks/2/comments"
data = {"content": "This is my first comment", "author": "Sonali"}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
