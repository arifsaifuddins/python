# encapsulation / visibility

# private __word (two underscors)
# proteccted _word (oone underscor)

class Kitab:

  def __init__(self, judul, halaman):

    self.judul = judul
    self.halaman = halaman

    # protected
    self._harga = 200000

    # private (access in class)
    self.__toko = 'arin'

  def cektoko(self):
    return self.__toko


class Buku:

  judul = Kitab('janji', 19).judul


safinah = Kitab('safinah', 33)
api = Buku()

# cant access privated property
# print(safinah.__toko)

# can access protected property
print(safinah._harga)

print(safinah.cektoko())
print(api.judul)
