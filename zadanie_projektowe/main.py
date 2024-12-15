from rozgrywka import Rozgrywka
from konfigurator import gracz1, gracz2

def main():
    Rozgrywka.uruchom_gre()
    while not Rozgrywka.czy_koniec():
        Rozgrywka.wykonaj_turę(gracz1, gracz2)
        if Rozgrywka.czy_koniec(): break
        Rozgrywka.wykonaj_turę(gracz2, gracz1)
    Rozgrywka.zakoncz_gre()

if __name__== '__main__':
    main()