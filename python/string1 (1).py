#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.

# Alapvető sztring műveletek
# Írjuk meg az alábbi függvények törzsét. A main() fv.
# már készen van s ezeket a fv.-eket hívja meg különböző
# paraméterekkel. Ha egy fv.-t helyesen írtunk meg, akkor
# az 'OK' üzenet jelenik meg.
# A fv.-eknek vmilyen értéket kell visszaadniuk, ezt a 'return'
# után adjuk meg.


# A. donuts
# Bemenet: egy egész szám (a fánkok száma).
# Adjunk vissza egy sztringet a köv. formában: 'Fánkok száma: <count>',
# ahol <count> a bemenetként kapott érték.
# Viszont ha a fánkok száma 10 vagy több, akkor a tényleges szám helyett
# a 'sok' szót használjuk.
# Vagyis donuts(5) visszatérési értéke 'Fánkok száma: 5', míg
# donuts(23) visszatérési értéke 'Fánkok száma: sok'
def donuts(count):
    if count < 10:
        return 'Fánkok száma: ' + str(count)
    # endif
    return 'Fánkok száma: sok'



# B. both_ends
# Egy adott s sztring esetén adjunk vissza egy olyan sztringet,
# mely az eredeti sztring első 2 és utolsó 2 karakteréből áll.
# Vagyis 'spring' esetén a visszatérési érték 'spng'.
# Ha az input sztring hossza 2-nél rövidebb, akkor egy üres
# sztringet adjunk vissza.
def both_ends(s):
    if len(s) < 2:
        return ''
    # endif
    return s[0:2] + s[-2:]


# C. fix_start
# Egy adott s sztring esetén adjunk vissza egy olyan sztringet,
# melyben az első karakter összes előfordulása helyén egy '*'
# szerepel, kivéve a legelső pozíciót.
# Példa: 'babble' => 'ba**le'
# Feltételezhetjük, hogy a bemeneti sztring hossza legalább 1.
# Tipp: s.replace(stra, strb) egy olyan sztringet ad vissza,
# melyben az stra összes előfordulása ki van cserélve strb-re.
def fix_start(s):
    fs = s[0:1]
    s2 = s[1:]
    if s2.find(fs) > -1:
        return fs + s2.replace(fs, '*')
    # endif
    return s


# D. MixUp
# Adott két bemeneti sztring, a és b. Adjunk vissza egyetlen sztringet,
# melyben a és b konkatenálva van úgy, hogy köztük egyetlen szóköz szerepel.
# Ezen túl cseréljük fel a két sztring első két karakterét az eredményben.
# Példa:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Feltételezhetjük, hogy a bemeneti sztringek hossza legalább 2.
def mix_up(a, b):
    ftChar1 = a[0:2]
    ftChar2 = b[0:2]
    return ftChar2 + a[2:] + " " + ftChar1 + b[2:]


# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    print('donuts')
    # Minden egyes sor meghívja a donuts() fv.-t s összehasonlítja a visszaadott
    # értéket a várt eredménnyel.
    text1 = " fánk esetén: "
    print("4" + text1, donuts(4))
    print("9" + text1, donuts(9))
    print("10" + text1, donuts(10))
    print("99" + text1, donuts(99))


    print()
    print('both_ends')
    print("A {0} szó esetén az eredmény: {1}".format("spring", both_ends('spring')))
    print("A {0} szó esetén az eredmény: {1}".format("Hello", both_ends('Hello')))
    print("A {0} szó esetén az eredmény: {1}".format("a", both_ends('a')))
    print("A {0} szó esetén az eredmény: {1}".format("xyz", both_ends('xyz')))


    print()
    print('fix_start')
    print("A {0} szó esetén az eredmény: {1}".format("babble", fix_start('babble')))
    print("A {0} szó esetén az eredmény: {1}".format("aardvark", fix_start('aardvark')))
    print("A {0} szó esetén az eredmény: {1}".format("google", fix_start('google')))
    print("A {0} szó esetén az eredmény: {1}".format("donut", fix_start('donut')))

    print()
    print('mix_up')
    print("A kapott szavaK: {0}, {1}. Az eredmény: {2}".format("mix", "pod", mix_up('mix', 'pod')))
    print("A kapott szavaK: {0}, {1}. Az eredmény: {2}".format("dog", "dinner", mix_up('dog', 'dinner')))
    print("A kapott szavaK: {0}, {1}. Az eredmény: {2}".format("gnash", "sport", mix_up('gnash', 'sport')))
    print("A kapott szavaK: {0}, {1}. Az eredmény: {2}".format("pezzy", "firm", mix_up('pezzy', 'firm')))
    

#############################################################################

if __name__ == '__main__':
    main()