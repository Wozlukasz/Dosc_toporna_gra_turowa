from jednostka import Jednostka
from abc import ABC, abstractmethod

class Lucznik(Jednostka):
    def __init__(self, imie):
        super().__init__(imie,50,30,3,3)
        '''zdrowie, sila_ataku, zasieg_ataku, szybkosc_ruchu'''




