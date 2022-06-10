import requests
import re
response = requests.get('https://reqres.in/api/users?page=2')
data = response.json()
for d in data['data']:
    assert d['id']
    assert d['email']
    assert d['first_name']
    assert d['last_name']
    assert d['avatar']
for d in data['data']: 
    assert '@reqres.in' in d['email']