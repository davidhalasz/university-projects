from ekezet import without_dic, with_dic

def test_without_dic():
    assert without_dic('á') == 'a'
    assert without_dic('é') == 'e'
    assert without_dic('í') == 'i'
    assert without_dic('ö') == 'o'
    assert without_dic('ő') == 'o'
    assert without_dic('ú') == 'u'
    assert without_dic('ü') == 'u'
    assert without_dic('ű') == 'u'

def test_with_dic():
    assert without_dic('á') == 'a'
    assert without_dic('é') == 'e'
    assert without_dic('í') == 'i'
    assert without_dic('ö') == 'o'
    assert without_dic('ő') == 'o'
    assert without_dic('ú') == 'u'
    assert without_dic('ü') == 'u'
    assert without_dic('ű') == 'u'