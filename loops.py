# loops

# for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i in numbers:
  print(i)

# break
for i in numbers:
  if i == 3:
    break
  print(i)

# continue
for i in numbers:
  if i == 5:
    continue
  print(i)

# range
for i in range(len(numbers)):
  print(i)

for i in range(1, 4):
  print(i)


# while
count = 0

while count <= 10:
  print(count)
  count += 1
