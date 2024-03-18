from os import sep
class Zlomok:

  def __init__(self, cit, men):
    self.__citatel = cit
    self.__menovatel = men

  def __str__(self):
    return self.__vypis()

  # čistá funkcia, nemení obsah
  def __vypis(self):
    return f'{self.__citatel}/{self.__menovatel}'

  def get_citatel(self):
    return self.__citatel

  def get_menovatel(self):
    return self.__menovatel

  # modifikátor, mení hodnotu atribútov

  def zmen_menovatel(self, hodnota):
    if hodnota != 0:
      self.__menovatel = hodnota
      return True
    else:
      return False

  # kopia .. klonovanie
  def kopia(self):
    z = Zlomok(self.__citatel, self.__menovatel)
    return z

  # sucin
  def sucin(self, iny):
    c = self.__citatel * iny.get_citatel()
    m = self.__menovatel * iny.get_menovatel()
    novy = Zlomok(c, m)
    return novy
    # chýba súčet, podiel a rozdieľ

  # porovnajme dva zlomky, ==
  def __eq__(self, iny):
    if not isinstance(iny, Zlomok):
      return None

    c = self.__citatel == iny.get_citatel()
    m = self.__menovatel == iny.get_menovatel()
    return c and m


  def __lt__(self, iny):
    if not isinstance(iny, Zlomok):
      return NotImplemented

    return (self.__citatel * iny.get_menovatel()) < (iny.get_citatel() * self.__menovatel)

  def __le__(self, iny):
    if not isinstance(iny, Zlomok):
      return NotImplemented

    return self.__lt__(iny) or self.__eq__(iny)


  def __gt__(self, iny):
    if not isinstance(iny, Zlomok):
      return NotImplemented

    return not (self.__le__(iny))

  def __ge__(self, iny):
    if not isinstance(iny, Zlomok):
      return NotImplemented

    return not (self.__lt__(iny))

  # chýba <, >, <=, >=, !=
  # ak zavolám zlomok * zlomok
  def __mul__(self, iny):
    if not isinstance(iny, Zlomok):
      return None

    c = self.__citatel * iny.get_citatel()
    m = self.__menovatel * iny.get_menovatel()
    novy = Zlomok(c, m)
    novy.zakladny_tvar()
    return novy

  def __add__(self, iny):
    if not isinstance(iny, Zlomok):
      return None

    c = self.__citatel * iny.get_menovatel() + iny.get_citatel() * self.__menovatel
    m = self.__menovatel * iny.get_menovatel()
    novy = Zlomok(c, m)
    novy.zakladny_tvar()
    return novy

    # rozdiel
  def __sub__(self, iny):
    if not isinstance(iny, Zlomok):
      return None

    c = self.__citatel * iny.get_menovatel() - iny.get_citatel() * self.__menovatel
    m = self.__menovatel * iny.get_menovatel()
    novy = Zlomok(c, m)
    novy.zakladny_tvar()
    return novy

  def __truediv__(self, iny):
      if not isinstance(iny, Zlomok):
          return None

      c = self.__citatel * iny.get_menovatel()
      m = self.__menovatel * iny.get_citatel()
      novy = Zlomok(c, m)
      novy.zakladny_tvar()
      return novy
    # súčin
  # chýba __add__ __sub__ __div__

  # čo keď ku zlomku +, -, *, / celé číslo?
  # napríklad 3/2 * 5

  # float
  def __float__(self):
     return(round(self.__citatel / self.__menovatel, 2))

  def __NSD(self, a, b):
    while a != b:
      if a > b:
        a -= b
      else:
        b -= a
    return a

  # uprava na zakladny
  def zakladny_tvar(self):
    nsd = self.__NSD(self.__citatel, self.__menovatel)
    self.__citatel //= nsd
    self.__menovatel //= nsd




z = Zlomok(10,13)
print(type(z))

print(dir(z))

z2 = Zlomok(5, 10)
#print(z.citatel)
#print(z2.menovatel)
#z.menovatel = 0
#print(z.vypis())
print(z.zmen_menovatel(9))
#print(z.vypis())
print(z.zmen_menovatel(0))
#print(z.vypis())

print(z)
print(z2)

klon = z.kopia()
print(klon)

sucin = z.sucin(z2)
print(sucin)

sucin = z * z2

print(sucin)

# porovnanie, prekryjem __eq__
# z == z2

print(float(sucin))
print(z == klon)
print(z == z2)

o = z * 3
print (o)