# methods

class Mahasiswa:

  # construct
  def __init__(self, nama, umur, kuliah, uang):

    # instance attribute
    self.nama = nama
    self.umur = umur
    self.kuliah = kuliah
    self.uang = uang

  def kenal(self):
    return f'Hi saya {self.nama}, saya kuliah {self.kuliah}'

  # special mehods (execute auto)
  def __str__(self):
    info = f'nama = {self.nama}, umur = {self.umur}, kuliah = {self.kuliah}, uang = {self.uang}'
    return info

  # change val
  def ubahUang(self, umur):
    if umur < 20:
      self.uang = 2000
      return self.uang
    elif umur >= 20:
      self.uang = 5000
      return self.uang
    elif umur == 30:
      self.uang = 6000
      return self.uang
    else:
      return self.uang


# instances
arief = Mahasiswa('arief', 32, 'tik', 200000)


print(arief.kenal())
print(arief)
print(arief.ubahUang(4))
print(arief.ubahUang(arief.umur))
