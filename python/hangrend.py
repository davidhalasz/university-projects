#!/usr/bin/env python3

#A szkript eldönti, hogy az adott szó milyen hangrendű.
MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

def hangrend(szavak, i):
    t_magas = False
    t_mely = False
    szo = list(szavak[i])
    mely = list(MELY_MGHK)
    magas = list(MAGAS_MGHK)
        
    for j in range(0, len(mely)):
        if (mely[j] in szo):
            t_mely = True

    for k in range(0, len(mely)):
        if (magas[k] in szo):
            t_magas = True
        
    if (t_mely and t_magas):
        return('A(z) "{0}" szó vegyes hangrendű.'.format(szavak[i]))
    elif (t_mely):
        return('A(z) "{0}" szó mély hangrendű.'.format(szavak[i]))
    elif (t_magas):
        return('A(z) "{0}" szó magas hangrendű.'.format(szavak[i]))
    else:
        return('A(z) "{0}" szó semmilyen hangrendű.'.format(szavak[i]))        
    

def main():
    i = 0
    szavak = ["ablak", "erkély", "kisvasút", "magas", "mély", "pffff"]
    while i < len(szavak):
        print(hangrend(szavak, i))
        i += 1
 

if __name__ == "__main__":
    main()