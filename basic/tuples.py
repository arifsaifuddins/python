# tuples unchageble

numbers = (1, 2, 3, 4, 5, 6)
# numbers = tuple((1,2,3,4,5,6))

fruits = ('mango', 'apple', 'orange', 'strawb')

print(type(fruits))

print(fruits[3])

# # cant chage
# fruits[2] = 'oke'

# delete
del numbers


# set tuple
fruits_set = {'mango', 'apple', 'orange', 'strawb'}

fruits_set.add('grape')
fruits_set.remove('apple')

fruits_set.clear()

print(fruits_set)
