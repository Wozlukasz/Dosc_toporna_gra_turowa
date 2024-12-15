from plansza import plansza
from jednostka import Jednostka
from opcje import Opcje



from gracz import Gracz
import os

class Ruch:
    # dół, lewo, prawo, góra zgodnie z kierunkami na klawiaturze numerycznej
    _kierunki = (5, -1, 1, -5)
    _wspolrzedne = (10, -1, 1, -10)

    @staticmethod
    def porusz_jednostke(gracz: Gracz):
        jednostka: Jednostka = gracz.jednostki[Opcje.wybierz_jednostke(gracz.moje_jednostki(), Rozgrywka.policz_zywych(gracz))]
        if jednostka.czy_zyje():
            pozycja_poczatkowa = plansza.znajdz_na_planszy(jednostka)
            poz0 = pozycja_poczatkowa
            while True:
                os.system('cls')
                gracz.wypisz_status_bonus('ruch:','szybkosc')
                print()
                plansza.wyswietl()
                
                
                pozycja_nowa = Ruch.oblicz_pozycje(pozycja_poczatkowa, wyjscie := Ruch.wprowadz_wartosc()) #wprowadzenie kierunku
                if wyjscie == -2: break
                elif pozycja_nowa != pozycja_poczatkowa:
                    if plansza.oblicz_dystans_int(Ruch.indeks_na_koodrynaty(poz0), Ruch.indeks_na_koodrynaty(pozycja_nowa)) <= jednostka.pobierz_dane_jednostki()['szybkosc']: # sprawdzenie czy odległość jest <= szybkości postaci
                        if plansza.dodaj_jednostke(jednostka, pozycja_nowa): #wewnątrz funkcji sprawdzana jest kolizja. Jeżeli dodanie się powiedzie zwraca wartość true
                            plansza.usun_jednostke(pozycja_poczatkowa)
                            pozycja_poczatkowa = pozycja_nowa
                            #wyswietl plansze i opis (najlepiej z kolorkami co jest jescze dostępne)
                            #zaaktualizuj pozycję poczatkową
                
        else: print('wprowadzono nieprawidłową wartość!') 
            
            #komunikat o błędzie
        
    
    @staticmethod
    def oblicz_pozycje(pozycja_poczatkowa, kierunek):
        if kierunek > -1 and kierunek < 4: 
            nowa_pozycja = pozycja_poczatkowa + Ruch._kierunki[kierunek]
            if Ruch.czy_na_planszy(nowa_pozycja):
                return nowa_pozycja
        #print("podano nieprawidłową wartość") 
        return pozycja_poczatkowa
        
    @staticmethod
    def wprowadz_wartosc():
        print('\n-------------------------------')
        kierunek = input('Poruszaj się używając strzałek\nklawiatury numerycznej(2,4,6,8)\n- Aby zakończyć wciśnij enter -')
        if kierunek.isdigit(): 
            if int(kierunek) in (4,2,6,8):
                return int(kierunek)//2-1
        elif kierunek == '':
            return -2
        #print("podano nieprawidłową wartość")
        return -1
    
    @staticmethod
    def czy_na_planszy(pozycja_nowa):
        poz = Ruch.indeks_na_koodrynaty(pozycja_nowa)
        if poz%10>4 or poz<0 or poz>44: 
            print("Nie można wyjść po za planszę!!")
            return False
        else: return True

    @staticmethod
    def indeks_na_koodrynaty(pozycja):
        return (pozycja)%10%5 + 10*((pozycja)//5)
    

#Ruch.porusz_jednostke(gracz1)
from rozgrywka import Rozgrywka