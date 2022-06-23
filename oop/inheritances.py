# inheritance extends

# parent class
class Parent:

  def mahasiswa(self):
    return 'hello world'.upper()

  name = 'lina'


# child class
class Child(Parent):

  def __init__(self, name):
    self.name = name


# child child
class mahasiswa1(Child):

  # override
  def __init__(self, name, age):
    # from Child class
    super().__init__(name)
    self.age = age

  def work(self):
    return f'hi iam {self.name}, iam working on IUA'


class mahasiswa2(Child):

  def __init__(self, name, kerja):
    # override
    super().__init__(name)
    self.kerja = kerja

  def work(self):
    return f'hi iam {self.name}, iam working on {self.kerja}'


class mahasiswa3(Child):

  def __init__(self, name, kuliah):
    # override
    super().__init__(name)
    self.kuliah = kuliah

  def work(self):
    return f'hi iam {self.name}, iam working on Quran, and in {self.kuliah} major'


# instance
lina = Parent()
arief = Child('arief')
adi = mahasiswa1('adi', 34)

print(arief.mahasiswa())  # access from parent
print(lina.name)
print(adi.name)


# polymophism
mhs = [
    mahasiswa1('arief', 32),
    mahasiswa2('odi', 'pabrik apple'),
    mahasiswa3('aman', 'islamic')
]


def mahasiswas(mhs):
  for m in mhs:
    print(m.work())


mahasiswas(mhs)
