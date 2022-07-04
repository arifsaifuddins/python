import requests


# GET

# with argument
res = requests.get('http://localhost:2003/get-student?api_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFsZmFAbWFpbC5jb20iLCJuYW1lIjoiYXJpZWYifQ.GEYubEH-tXlfPfjCZq_66IvKT_SnmZyLlVMXvt5-h_A')

param = {'api_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFsZmFAbWFpbC5jb20iLCJuYW1lIjoiYXJpZWYifQ.GEYubEH-tXlfPfjCZq_66IvKT_SnmZyLlVMXvt5-h_A'}
respo = requests.get('http://localhost:2003/get-student', params=param)


# with headers
header = {'key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFsZmFAbWFpbC5jb20iLCJuYW1lIjoiYXJpZWYifQ.GEYubEH-tXlfPfjCZq_66IvKT_SnmZyLlVMXvt5-h_A'}
resp = requests.get('http://localhost:2003/get-student', headers=header)

# print(res.json())
# print(resp.json())
print(respo.json())


# POST

user = {'name': 'ariefssss', 'email': 'ar@mail.com', 'password': 'qwerty'}
register = requests.post('http://localhost:2003/register', data=user)

user = {'email': 'ar@mail.com', 'password': 'qwerty'}
login = requests.post('http://localhost:2003/login', data=user)

print(register.json())
print(login.json())


# PUT

student = {'name': 'ariefssss', 'email': 'ar@mail.com', 'poster': 'qwerty.jpg'}
userstudent = requests.put(
    'http://localhost:2003/put-student/10',
    data=student
)

print(userstudent.json())


# DELETE

# delstudent = requests.delete(
#     'http://localhost:2003/del-student/1'
# )

# print(delstudent.json())
