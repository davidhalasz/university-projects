#!/usr/bin/env python3
from enum import Enum

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

class HangrendEnum(Enum):
    MELY = 1
    MAGAS = 2
    VEGYES = 3
    SEMMILYEN = 4

class Hangrend():
    
    def ch_hr(self, word):
        t_magas = False
        t_mely = False
        number = 0
        szo = list(word)
        mely = list(MELY_MGHK)
        magas = list(MAGAS_MGHK)
            
        for j in range(0, len(mely)):
            if (mely[j] in szo):
                t_mely = True

        for k in range(0, len(mely)):
            if (magas[k] in szo):
                t_magas = True
            
        if (t_mely and t_magas):
            return HangrendEnum.VEGYES.name
        elif (t_mely):
            return HangrendEnum.MELY.name
        elif (t_magas):
           return HangrendEnum.MAGAS.name
        else:
            return HangrendEnum.SEMMILYEN.name


def main():
    h = Hangrend()
    szavak = ["ablak", "erkély", "kisvasút", "magas", "mély", "pffff"]

    for szo in szavak:
        hangrend = ""
        if (h.ch_hr(szo) == "VEGYES"):
            hangrend = "vegyes"
        elif (h.ch_hr(szo) == "MELY"):
            hangrend = "mély"
        elif (h.ch_hr(szo) == "MAGAS"):
            hangrend = "magas"
        else:
            hangrend = "semmilyen"    
        print('A(z) "{0}" szó {1} hangrendű.'.format(szo, hangrend))
 

if __name__ == "__main__":
    main()