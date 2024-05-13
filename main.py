import os
from abc import ABC, abstractmethod
from datetime import datetime


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def szolgaltatasok(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar=50):
        super().__init__(ar, szobaszam=szobaszam)
        self.foglalasok = []

    def szolgaltatasok(self):
        return "TV, zuhanyzó, egyágyas ágy"


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar=80):
        super().__init__(ar, szobaszam=szobaszam)
        self.foglalasok = []

    def szolgaltatasok(self):
        return "TV, zuhanyzó, kétágyas ágy"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        today = datetime.today()
        if datum <= today:
            print("A foglalás dátuma nem lehet múltbeli vagy a mai nap!")
            return None
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

    def lemondas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in szoba.foglalasok:
                    if foglalas.datum == datum:
                        szoba.foglalasok.remove(foglalas)
                        print("A foglalás sikeresen lemondva!")
                        return
                print("Nincs ilyen foglalás ezen a dátumon!")
                return
        print("Nincs ilyen szoba!")
        return

    def osszes_foglalas(self):
        foglalasok = []
        for szoba in self.szobak:
            for foglalas in szoba.foglalasok:
                foglalasok.append(foglalas)
        return foglalasok


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás: Szoba {self.szoba.szobaszam}, Dátum: {self.datum.strftime('%Y-%m-%d')}"


def main():
    szalloda = Szalloda(nev="Luxus Hotel")

    egyagyas = EgyagyasSzoba(szobaszam="A101")
    ketagyas = KetagyasSzoba(szobaszam="B202")

    szalloda.uj_szoba(egyagyas)
    szalloda.uj_szoba(ketagyas)

    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Adja meg a választott művelet számát: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            ar = szalloda.foglalas(szobaszam, datum)
            if ar is not None:
                print(f"A foglalás sikeres! Az ár: {ar}")

        elif valasztas == "2":
            szobaszam = input("Adja meg a szobaszámot: ")
            datum_str = input("Adja meg a lemondás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            szalloda.lemondas(szobaszam, datum)

        elif valasztas == "3":
            foglalasok = szalloda.osszes_foglalas()
            if foglalasok:
                print("Összes foglalás:")
                for foglalas in foglalasok:
                    print(foglalas)
            else:
                print("Nincsenek foglalások.")

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")


if __name__ == "__main__":
    main()
