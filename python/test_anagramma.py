from anagramma import normalize, anagramma

def test_normailze():
    assert normalize("Clint Eastwood") == "clinteastwood"

def test_anagramma():
    assert anagramma("listen", "silent") == True
    assert anagramma("A gentleman", "Elegant man") == True
    assert anagramma("korte", "alma") == False