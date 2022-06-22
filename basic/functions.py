# function

# with indentations
def sayHello(name='jhon'):
  return f'Hello {name}'


print(sayHello('arief'))


# return val
def getSum(num1, num2):
  total = num1*num2
  return total


sum = getSum(2, 3)
print(sum)


# lambda function like arrow func in js
# getTotal = lambda num1, num2: num1 - num2

# print(getTotal(3,5))
