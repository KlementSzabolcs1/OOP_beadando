from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def szolgaltatasok(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=50, szobaszam=szobaszam)
        self.agyasok_szama = 1

    def szolgaltatasok(self):
        return "TV, zuhanyzó, egyágyas ágy"


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=80, szobaszam=szobaszam)
        self.agyasok_szama = 2

    def szolgaltatasok(self):
        return "TV, zuhanyzó, kétágyas ágy"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in szoba.foglalasok:
                    if foglalas.datum == datum:
                        print("Ez a szoba már foglalt ezen a napon!")
                        return None
                szoba.foglalasok.append(Foglalas(szoba, datum))
                return szoba.ar
        print("Nincs ilyen szoba!")
        return None


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás: Szoba {self.szoba.szobaszam}, Dátum: {self.datum.strftime('%Y-%m-%d')}"


