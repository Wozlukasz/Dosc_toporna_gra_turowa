from abc import ABC, abstractmethod

class Jednostka(ABC):
    @abstractmethod
    def __init__(self, imie, zdrowie, sila_ataku, zasieg_ataku, szybkosc_ruchu):
        self._zdrowie = zdrowie
        self._sila_ataku = sila_ataku
        self._zasieg_ataku = zasieg_ataku
        self._szybkosc_ruchu = szybkosc_ruchu
        self.imie = imie

    def otrzymaj_obrazenia(self, obrazenia):
        self._zdrowie -= obrazenia
        if self._zdrowie < 0: self._zdrowie = 0

    def czy_zyje(self):
        if self._zdrowie:
            return True
        else: 
            return False
    
    def pobierz_dane_jednostki(self):
        return dict(zdrowie=self._zdrowie,
        sila=self._sila_ataku,
        zasieg=self._zasieg_ataku,
        szybkosc=self._szybkosc_ruchu,
        imie=self.imie)
    


