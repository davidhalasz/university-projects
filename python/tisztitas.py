#!/usr/bin/env python3

def clean(text):
    ctxt = "".join(text.split())

    return ctxt
    

def main():
    text = "206.130.99.82:\n 8080"
    print(clean(text))

##############################################################################

if __name__ == "__main__":
    main()