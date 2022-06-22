# string

name = 'arief'
age = 22

# concat
print('hello, my name is ' + name + ' and i ' + str(age) + ' old')

# string argument format
print('hello, my name is {name}, and i {age} old'.format(name=name, age=age))

# f-string
print(f'hello, my name is {name}, and i {age} old')

# string methods
s = 'hello arief'

# capitalize
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.endswith())
print(s.split())
print(s.isalnum())
print(s.isnumeric())
print(s.isalpha())
print(len(s))
print(s.find('o'))
print(s.count('l'))
print(s.replace('arief', 'joni'))
