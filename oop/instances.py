# instance & construct

class Mahasiswa:

  # class attribute
  mahasiswa = 'Arief Saifuddien Supadi'

  # construct
  def __init__(self, nama, umur, kuliah, uang):

    # instance attribute
    self.nama = nama
    self.umur = umur
    self.kuliah = kuliah
    self.uang = uang


# instances
arief = Mahasiswa('arief', 32, 'tik', 200000)

print(arief.mahasiswa)
