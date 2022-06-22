# conditions

x = 4
y = 3

# ==, !=, >, <, >=, <=
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')
else:
  print(f'{x} is not equal {y}')


# nested cond
if x == 4:
  if x > y:
    print('x is greater than y')

# and, or, not, in, is
numbers = [1, 2, 3, 4, 5, 6, 7]

if x == numbers[3] and 3 < x:
  print('right')

if x == numbers[3] or 3 < x:
  print('right')


if not(x == y):
  print(f'{x} not equal')

if not x == y:
  print(f'{x} not equal')

if x in numbers:
  print(True)

if y is numbers[2]:
  print(True)
