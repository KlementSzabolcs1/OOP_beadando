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
