from zarojelek import check

def test_check():
    assert check("((5+3)*2+1)") == True
    assert check("{[(3+1)+2]+}") == True
    assert check("(3+{1-1)}") == False
    assert check("[1+1]+(2*2)-{3/3}") == True
    assert check("(({[(((1)-2)+3)-3]/3}-3)") == False
