#!/usr/bin/env python3

# A szkript eldönti, hogy teljesül-e az, 
# hogy az egyik változó igazként míg a másik hamisként értékelődik ki.
def xor(s1, s2):
    if(bool(s1) == bool(s2)):
        print("Az igaz-hamis feltétel nem teljesül!")
    else:
        print("Az igaz-hamis feltétel teljesül!")


def main():
    str1 = "python"
    str2 = None
    print("A két változó értékei: \"python\" és None. Az eredmény:")
    xor(str1, str2)   

    str3 = "alma"
    str4 = "körte"
    print("\nA két változó értékei: \"alma\" és \"körte\". Az eredmény:")
    xor(str3, str4)  


if __name__ == "__main__":
    main()