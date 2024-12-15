from jednostka import Jednostka
import math

class Plansza:
    def __init__(self):
        self.pola = dict()
        for n in range(25):
            self.pola[n] = 0 # przelicznik x i y na wartość: y*5+x
# do dokończenia

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Plansza, cls).__new__(cls)
            Plansza()
        return cls._instance


    def kolizja(self, pozycja):
        if self.pola[pozycja] == 0: return False
        else:
            #print("\nDane pole jest już zajęte!\n") 
            return True

    def dodaj_jednostke(self, jednostka: Jednostka, pozycja):
        if not self.kolizja(pozycja):
            self.pola[pozycja] = jednostka   
            return True
        return False
            
    def znajdz_na_planszy(self, jednostka: Jednostka):
        for elem in self.pola.items():
            if elem[1] == jednostka: return elem[0]

    def wyswietl(self):
        n=1
        for element in self.pola.values():
            if type(element) == int: print(element, end="  ")
            else: 
                if element.czy_zyje():
                    print(element.pobierz_dane_jednostki()['imie'], end=" ") 
                else: print('X', end='  ')
            if not n%5: print()
            n+=1

    def oblicz_dystans(self, jednostka1: Jednostka, jednostka2: Jednostka):
        poz1 = self.znajdz_na_planszy(jednostka1)%10%5 + 10*(self.znajdz_na_planszy(jednostka1)//5)
        poz2 = self.znajdz_na_planszy(jednostka2)%10%5 + 10*(self.znajdz_na_planszy(jednostka2)//5)
        dyst_x = (poz2%10 - poz1%10)
        dyst_y = (poz2//10 - poz1//10)
        return math.floor(math.sqrt(dyst_x**2 + dyst_y**2))
    
    def oblicz_dystans_int(self, poz1: int, poz2: int):
        dyst_x = (poz2%10 - poz1%10)
        dyst_y = (poz2//10 - poz1//10)
        return math.floor(math.sqrt(dyst_x**2 + dyst_y**2))
    
    def usun_jednostke(self, pozycja):
        plansza.pola[pozycja] = 0
    
plansza = Plansza()