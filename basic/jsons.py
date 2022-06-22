# json and dicts
import json

mhs = '{"name":"arief", "age":"22"}'
mhs1 = {'name': 'arief', 'age': 22}

# convert to dict
m = json.loads(mhs)

# convert to json
v = json.dumps(mhs1)

print(m)
print(v)
