# class oop

# create class
class Users:

  # constracts
  def __init__(self, name, age, email):

    # properties in constract
    self.name = name
    self.age = age
    self.email = email

  # properties
  parent = 'supadi'

  # methods
  def greating(self):
    return f'Hello everyone!, my name is {self.name}, and i {self.age} old, and my parent is {self.parent}'


# extend class
class Customer(Users):

  def __init__(self, name, age, email):

    self.name = name
    self.age = age
    self.email = email
    self.place = '' or self.setPlace()

  def setPlace(self):
    return 'Jepara'

  def greating(self):
    self.place = 'Sudan'

    return f'Hello everyone!, my name is {self.name}, and i {self.age} old, andi from {self.place}'


# init an object
arief = Users('Arief Saifuddien', 32, 'arief@mail.com')
ani = Customer('Ani', 22, 'ani@mail.com')


print(arief.greating())

# get from user class when no method same in child class
print(ani.greating())
