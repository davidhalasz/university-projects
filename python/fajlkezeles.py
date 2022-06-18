#!/usr/bin/env python3


def main():
    fr = open("string1.py", "r")
    lines = fr.readlines()
    fw = open("string1_clean.py", "w")

    for line in lines:
        if not line.startswith("#") and not line.startswith("    #") or line.startswith("#!"):
            fw.write(line)

    fr.close()
    fw.close()

##############################################################################

if __name__ == "__main__":
    main()