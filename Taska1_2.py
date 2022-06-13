<<<<<<< HEAD
import requests
url='https://reqres.in/api/users'
myobj={"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth"}
response = requests.post(url,data=myobj)
data = response.json()

assert response.status_code == 201, 'Wrong status code'
assert myobj['email'] == data['email'], 'Wrong email'
assert myobj['first_name'] == data['first_name'], 'Wrong first_name'
assert myobj['last_name'] == data['last_name'], 'Wrong last_name'
=======
import requests
url='https://reqres.in/api/users'
myobj={"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth"}
response = requests.post(url,data=myobj)
data = response.json()

assert response.status_code == 201, 'Wrong status code'
assert myobj['email'] == data['email'], 'Wrong email'
assert myobj['first_name'] == data['first_name'], 'Wrong first_name'
assert myobj['last_name'] == data['last_name'], 'Wrong last_name'
>>>>>>> 284fa9a303f6c94a54686f95425cf88d11387f03
