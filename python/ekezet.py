#!/usr/bin/env python3

TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
"""

def without_dic(text):
    ekezetek = list("áéíóöőúüűÁÉÍÓÖŐÚÜŰ")
    lst = []
    for t in text:
        if t in ekezetek:
            if t == 'á':
                lst.append('a')
            if t == 'é':
                lst.append('e')
            if t == 'í':
                lst.append('i')
            if t == 'ó' or t == 'ö' or t == 'ő':
                lst.append('o')
            if t == 'ú' or t == 'ü' or t == 'ű':
                lst.append('u')
            if t == 'Á':
                lst.append('A')
            if t == 'É':
                lst.append('É')
            if t == 'Í':
                lst.append('I')
            if t == 'Ó' or t == 'Ö' or t == 'Ő':
                lst.append('O')
            if t == 'Ú' or t == 'Ü' or t == 'Ű':
                lst.append('U')
        else:
            lst.append(str(t))
    res = "".join(lst)
    return res


def with_dic(text):
    d = {
        "á": "a", "é": "e",
        "í": "i", "ó": "o",
        "ö": "o", "ő": "o",
        "ú": "u", "ü": "u",
        "ű": "u", "Á": "A",
        "É": "E", "Í": "I",
        "Ó": "O", "Ö": "O",
        "Ő": "O", "Ú": "U",
        "Ü": "U", "Ű": "U"
    }
    lst = []
    for t in text:
        if t in d:
            lst.append(d.get(t))
        else:
            lst.append(t)
    res = "".join(lst)
    return res


def main():
    print("Szótár használata nélkül:")
    print(without_dic(TEXT))
    print("--------------------------------")
    print("Szótár használatával:")
    print(with_dic(TEXT))

##############################################################################

if __name__ == "__main__":
    main()