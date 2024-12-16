from gracz import Gracz
from lucznik import Lucznik
from rycerz import Rycerz
from kusznik import Kusznik
from piechur import Piechur
from plansza import plansza
# -------------------------------- OPIS ZASAD ---------------------------------------

# Gra polega na walce między jednostkami - wygrywa ten kto pokona wszystkie jednostki przeciwnika. 
# Dostępne są 4 jednostki (rycerz, łucznik, kusznik, piechur)
# Poszczególne statystyki można znaleźć w odpowiednich plikach danej jednostki
# 
# Gra odbywa się na zasadzie tur. W trakcie jednej tury można wykonać jednego ataku i poruszyć jedną jednostkę.
# 
# Aby skonfigurować swoją grę, usuń/dodaj komentarze przy odpowiednich jednostkach, dodaj je na planszę i dodaj imię gracza
# Powodzenia i miłej zabawy!


#------------------------------------------------------------------------------------ gracz 1

#'''Wprowadź imię jako argument'''
gracz1 = Gracz('lukasz')

#'''Wybierz 2 jednostki'''
l1 = Lucznik('l1')
r1 = Rycerz('r1')
#p1 = Piechur('p1')
#k1 = Kusznik('k1')

#'''wprowadź nazwy wybranych jednostek jako argumenty (dowolna kolejność)'''
gracz1.wezwij_jednostki(l1,r1)
plansza.dodaj_jednostke(l1, 5)
plansza.dodaj_jednostke(r1, 1)


#------------------------------------------------------------------------------------ gracz 2

#'''Wprowadź imię jako argument'''
gracz2 = Gracz('Albert')

#'''Wybierz 2 jednostki'''
l2 = Lucznik('l2')
r2 = Rycerz('r2')
#p2 = Piechur('p2')
#k2 = Kusznik('k2')

#'''wprowadź nazwy wybranych jednostek jako argumenty (dowolna kolejność)'''
gracz2.wezwij_jednostki(l2,r2)
plansza.dodaj_jednostke(l2, 19)
plansza.dodaj_jednostke(r2, 23)




