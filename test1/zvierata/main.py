import random


class Zviera:
    def __init__(self, m, v):
        # self.__meno = None
        # self.__vek = None
        self.set_meno(m)
        self.set_vek(v)
        self.set_zvuk(None)

    def get_meno(self):
        return self.__meno

    def get_vek(self):
        return self.__vek

    # zvuk nie je private ale protected, inak by sme ho nemohli priamo pouzivat v jeho potomkoch
    def set_zvuk(self, z):
        self._zvuk = z

    def set_meno(self, m):
        if m == "":
            raise ValueError("Meno nesmie byť prázdne")

        self.__meno = m[0].upper() + m[1:].lower()

    def set_vek(self, v):
        # if not isinstance(v, float)

        if type(v) not in [float, int]:
            raise ValueError("Zadaj číslo!")
        elif v <= 0:
            raise ValueError("Vek musí byť väčší ako nula!")
        self.__vek = v

    def info(self):
        return f"{self.__class__.__name__}: meno='{self.__meno}', vek='{self.__vek}', "

    def __str__(self):
        return self.info()

    def urob_zvuk(self):
        return self._zvuk


class Macka(Zviera):
    # neexistuje tu tzv. overloading, nie je možné vytvoriť viac ako jeden konštruktor __init__
    def __init__(self, m, v):
        # zavolám konšturktor predka
        super().__init__(m, v)
        self.set_zvuk("Mnau mnau")
        self.__nezavislost = random.uniform(0.5, 1.0)

    def lov(self):
        h = random.randrange(100)
        sanca = random.random() * self.__nezavislost
        return "Lovim." if sanca > 0.5 else "Nelovim"

    # polymofizmus = prekrývam metódu predka
    def info(self):
        return (
            super().info()
            + f"nezavislost='{round(self.__nezavislost, 4)}' zvuk='{self._zvuk}'"
        )

    def urob_zvuk(self):
        return self._zvuk

    def mnaukaj(self):
        return self.urob_zvuk()

    def __init__(self, m, v):
        # self.__meno = None
        # self.__vek = None
        self.set_meno(m)
        self.set_vek(v)
        self.set_zvuk(None)

    def get_meno(self):
        return self.__meno

    def get_vek(self):
        return self.__vek

    # zvuk nie je private ale protected, inak by sme ho nemohli priamo pouzivat v jeho potomkoch
    def set_zvuk(self, z):
        self._zvuk = z

    def set_meno(self, m):
        if m == "":
            raise ValueError("Meno nesmie byť prázdne")

        self.__meno = m[0].upper() + m[1:].lower()

    def set_vek(self, v):
        # if not isinstance(v, float)

        if type(v) not in [float, int]:
            raise ValueError("Zadaj číslo!")
        elif v <= 0:
            raise ValueError("Vek musí byť väčší ako nula!")
        self.__vek = v

    def info(self):
        return f"{self.__class__.__name__}: meno='{self.__meno}', vek='{self.__vek}', "

    def __str__(self):
        return self.info()

    def urob_zvuk(self):
        return self._zvuk


class Pes(Zviera):
    # neexistuje tu tzv. overloading, nie je možné vytvoriť viac ako jeden konštruktor __init__
    def __init__(self, m, v, p=None):
        # zavolám konšturktor predka
        super().__init__(m, v)
        self.set_zvuk("Hav hav")
        self.__poslusnot = p if p is not None else random.randrange(10)

    def aport(self):
        h = random.randint(1, 10)
        if self.__poslusnot > h:
            return "Aportujem."
        else:
            return "Nechce sami aportovat."

    # polymofizmus = prekrývam metódu predka
    def info(self):
        # zvuk viem pouzit priamo v potomkoch
        return super().info() + f" poslusnost='{self.__poslusnot}' zvuk='{self._zvuk}',"

    def urob_zvuk(self):
        return super().urob_zvuk()

    def stekaj(self):
        return self.urob_zvuk()


class Utulok:
    id_counter = 0

    def __init__(self):
        self.__miestonosti = []

    def add_zviera(self, z):
        self.__miestonosti.append(z)
        self.id_counter += 1

    def remove_zviera_idx(self, idx):
        if idx >= 0 and idx < len(self.__miestonosti):
            del self.__miestonosti[idx]

    def remove_zviera_obj(self, objZviera):

        if objZviera in self.__miestonosti:
            self.__miestonosti.remove(objZviera)

    def get_zviera(self, idx):
        if idx >= 0 and idx < len(self.__miestonosti):
            return self.__miestonosti[idx]

    def get_zvierata(self):
        return [zviera.get_meno() for zviera in self.__miestonosti]

    def get_cinnosti_zvierat(self):
        ls = []
        for zviera in self.__miestonosti:
            if isinstance(zviera, Pes):
                ls.append(zviera.aport())
            elif isinstance(zviera, Macka):
                ls.append(zviera.get_meno())
            elif isinstance(zviera, Slon):
                ls.append(zviera.zatrub())
        return ls

    def get_miestnosti(self):
        return self.__miestonosti

    def __str__(self):
        return " ".join(self.get_zvierata())

class Slon(Zviera):
    def __init__(self, m, v, dlzka_chobota):
        super().__init__(m, v)
        self.set_zvuk("tuuut")
        self.__dlzka_chobota = dlzka_chobota

    def info(self):
        return super().info() + f"zvuk='{self._zvuk}', dlzka_chobota='{self.__dlzka_chobota}'"

    def zatrub(self):
        return self.urob_zvuk()

    def zaslapni(self, pes):
        if isinstance(pes, Pes):
            del pes

if __name__ == "__main__":
    utulok = Utulok()
    utulok.add_zviera(Pes("dunco", 5))
    utulok.add_zviera(Slon("slon", 4, 6))
    utulok.add_zviera(Macka("macka", 5))
    print(utulok.get_cinnosti_zvierat())
    print(utulok.get_zvierata())
    print(utulok)
    print(utulok.get_miestnosti())
