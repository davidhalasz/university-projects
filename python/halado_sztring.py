#!/usr/bin/env python3

#Listában tárolt filmek és rendezők neveinek kiíratása haladó sztring formázás használatával.
def main():
    movies = [
        ("Star Wars: A New Hope", 1977, "George Lucas"),
        ("Avengers: Endgame", 2019, "Joe Russo, Anthony Russo"),
        ("Star Trek: Into Darkness", 2013, "J. J. Abrams"),
    ]
    
    print ("|" + "-"*76 + "|")
    print ("| {0:<24} | {1:^20} | {2:<24} |".format("Movie Title",
                                           "Release Date",
                                           "Director"))
    print ("|" + "-"*76 + "|")
    for element in movies:
        print ("| {0:<24} | {1:^20} | {2:<24} |".format(element[0], element[1], element[2]))
    print ("|" + "-"*76 + "|")


##############################################################################

if __name__ == "__main__":
    main()