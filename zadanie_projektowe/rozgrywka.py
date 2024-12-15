from gracz import Gracz
from konfigurator import gracz1, gracz2, plansza

import os
import time

class Rozgrywka:
    @staticmethod
    def wykonaj_turę(gracz: Gracz, oponent: Gracz):
        Opcje.wybierz_czynnosc(gracz, oponent)

        os.system('cls')
        print('---------------')
        print('Tura zakończona')
        print('---------------')
        time.sleep(1.5)
        
        

    @staticmethod
    def czy_koniec():
        if Rozgrywka.policz_zywych(gracz1) == 0 or Rozgrywka.policz_zywych(gracz2) == 0: return True
        
        
    @staticmethod
    def uruchom_gre():
        os.system('cls')
        gracz1.wypisz_status()
        print('\n')
        gracz2.wypisz_status()

        time.sleep(2.5)
        os.system('cls')

        print('----------------------------')
        print(f'Grę rozpoczyna {gracz1.imie}!')
        print('----------------------------')

        time.sleep(1.5)
        os.system('cls')


    @staticmethod
    def policz_zywych(gracz):
        liczba_zywych=0
        for jedn in gracz.jednostki:
            if jedn.czy_zyje():
                liczba_zywych+=1
        return liczba_zywych



    @staticmethod
    def zakoncz_gre():
        if Rozgrywka.policz_zywych(gracz2): zwyciezca = gracz2
        else: zwyciezca = gracz1
        print('-------------')
        print('To tyle...')
        print(f'wygrywa: {zwyciezca.imie}')
        print('-------------')
from opcje import Opcje