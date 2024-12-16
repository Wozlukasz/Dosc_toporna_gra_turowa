from walka import Walka
from gracz import Gracz
from plansza import plansza
import time
import os


class Opcje:
    @staticmethod
    def wybierz_czynnosc(gracz1: Gracz, gracz2: Gracz):
        decyzje = 0
        while True:
            os.system('cls')
            gracz1.wypisz_status()
            print()
            plansza.wyswietl()

            if decyzje != 3:
                wybor = input('\n----Wybierz czynność----\n1. Ruch\n2. Atak\nlub wciśnij enter by zakończyć turę...')
                if wybor == '':
                    break
                if int(wybor) == 1: 
                    if decyzje !=1:
                        Ruch.porusz_jednostke(gracz1)
                        decyzje +=1
                    else: 
                        print('wykonano już ruch!')
                        time.sleep(1.5)
                if int(wybor) == 2:
                    if decyzje != 2: 
                        Walka.wykonaj_atak(gracz1, gracz1.jednostki[Opcje.wybierz_jednostke(f'~~ atakujący ~~\n{gracz1.moje_jednostki()}', Rozgrywka.policz_zywych(gracz1))], gracz2.jednostki[Opcje.wybierz_jednostke(f'~~ cel ~~\n{gracz2.moje_jednostki()}', Rozgrywka.policz_zywych(gracz2))])
                        decyzje +=2
                        time.sleep(2.5)
                    else: 
                        print('wykonano już atak!')
                        time.sleep(2)
            else:
                input('\n----Wciśnij enter by zakończyć turę----')
                break

    @staticmethod
    def wybierz_jednostke(komunikat, liczba_opcji):
        wybor=0
        while True:
            wybor = input(f'\nWybierz jednostkę:\n{komunikat}')
           # if wybor.isdigit():
            if wybor.isdigit() and int(wybor) > 0 and int(wybor) <= liczba_opcji: break
            else: print("Wybrano nieprawidłową wartość, spróbuj ponownie.\n")
           # else: print("Wybrano nieprawidłową wartość, spróbuj ponownie.\n")

        return int(wybor)-1

from ruch import Ruch
from rozgrywka import Rozgrywka

