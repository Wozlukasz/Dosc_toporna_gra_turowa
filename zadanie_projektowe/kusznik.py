from jednostka import Jednostka

class Kusznik(Jednostka):
    def __init__(self, imie):
        super().__init__(imie, 80,40,2,1)
        '''zdrowie, sila_ataku, zasieg_ataku, szybkosc_ruchu'''

