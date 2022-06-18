#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """A fuggveny csak a valid karaktereket adja vissza, ha szerepel a sztringben."""
    lst_chr = list(chars)
    match = [c for c in lst_chr if c in text]
    result = "".join(match)
    print (result[::-1])

def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")

########################

if __name__ == "__main__":
    main()