# dictionary // like object and json

# create
person = {
    'name': 'arief',
    'age': 21,
    'place': 'sudan'
}

# use constructor
person2 = dict(name='arief', age=21)

print(person)

# get one val
print(person['age'])
print(person.get('place'))

# add val
person['phone'] = '02802-920209-22882'

print(person)
print(person.keys())
print(person.items())

# get copy
person1 = person.copy()
person1['is_student'] = True

print(person1)

# remove item
del(person['place'])
person1.pop('age')
person2.clear()

print(person)
print(person1)
print(person2)
