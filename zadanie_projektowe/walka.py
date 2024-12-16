from jednostka import Jednostka
from plansza import plansza
from konfigurator import gracz1, gracz2
import os



class Walka:
    @staticmethod
    def sprawdz_zasieg(atakujacy: Jednostka, cel: Jednostka):
        if atakujacy._zasieg_ataku >= plansza.oblicz_dystans(atakujacy, cel): return True 
        else: return False

    @staticmethod
    def oblicz_obrazenia(atakujacy: Jednostka, dystans):
        return int(atakujacy.pobierz_dane_jednostki()['sila']/dystans)

    @staticmethod
    def wykonaj_atak(gracz, atakujacy: Jednostka, cel: Jednostka):
        os.system('cls')
        gracz.wypisz_status_bonus('sila:','sila')
        plansza.wyswietl()
        print(f'\natak: {atakujacy.imie} -> {cel.imie}', end=' ')
        if gracz2.czy_moje(atakujacy) != gracz2.czy_moje(cel):
            if Walka.sprawdz_zasieg(atakujacy, cel):
                cel.otrzymaj_obrazenia(Walka.oblicz_obrazenia(atakujacy,plansza.oblicz_dystans(atakujacy, cel)))
                if not cel.czy_zyje():
                    if gracz2.czy_moje(cel):
                        gracz2.zmien_kolejnosc_jednostek()
                    else: gracz1.zmien_kolejnosc_jednostek()
                print('zakończył się sukcesem!')
            else: print('nie powiódł się...')
        

