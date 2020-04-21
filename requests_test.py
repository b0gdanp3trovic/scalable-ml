import requests

result = requests.post('http://localhost:5000', json = {'LSTAT' : 10, 'RM' : 30})
print(result.json())