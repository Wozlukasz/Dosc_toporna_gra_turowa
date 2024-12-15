from jednostka import Jednostka

class Gracz:
    def __init__(self, imie):
        self.jednostki = []
        self.imie = imie
    
    def wezwij_jednostki(self, jednostka1: Jednostka, jednostka2: Jednostka):
        self.jednostki.append(jednostka1)
        self.jednostki.append(jednostka2)

    def moje_jednostki(self):
        wypis = ''
        n=1
        for jednostka in self.jednostki:
            if jednostka.czy_zyje():
                wypis += f'{n}. {jednostka.pobierz_dane_jednostki()["imie"]}\n'
                n+=1
        return wypis

    def wypisz_status_bonus(self, komunikat, dana):
        # print('-------------------')
        print(f'----- Gracz: {self.imie} -----')
        #print(f'Dostępne jednostki:')
        print(f'\n-> {self.jednostki[0].pobierz_dane_jednostki()["imie"]} {self.jednostki[0].pobierz_dane_jednostki()["zdrowie"]}hp, {self.jednostki[0].pobierz_dane_jednostki()["sila"]}dp, {komunikat} {self.jednostki[0].pobierz_dane_jednostki()[dana]} pola')
        print(f'-> {self.jednostki[1].pobierz_dane_jednostki()["imie"]} {self.jednostki[1].pobierz_dane_jednostki()["zdrowie"]}hp,  {self.jednostki[1].pobierz_dane_jednostki()["sila"]}dp, {komunikat} {self.jednostki[1].pobierz_dane_jednostki()[dana]} pola')
        print('---------------------------')

    def wypisz_status(self):
        # print('-------------------')
        print(f'----- Gracz: {self.imie} -----')
        print(f'Dostępne jednostki:')
        print(f'-> {self.jednostki[0].pobierz_dane_jednostki()["imie"]} {self.jednostki[0].pobierz_dane_jednostki()["zdrowie"]}hp, {self.jednostki[0].pobierz_dane_jednostki()["sila"]}dp')
        print(f'-> {self.jednostki[1].pobierz_dane_jednostki()["imie"]} {self.jednostki[1].pobierz_dane_jednostki()["zdrowie"]}hp, {self.jednostki[1].pobierz_dane_jednostki()["sila"]}dp')

    def czy_moje(self, jednostka: Jednostka):
        return jednostka in self.jednostki


