tunnus = "python"
salasana = "rules"

while True:
    syote_tunnus = input("Anna käyttäjätunnus: ")
    syote_salasana = input("Anna salasana: ")

    if syote_tunnus == tunnus and syote_salasana == salasana:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
