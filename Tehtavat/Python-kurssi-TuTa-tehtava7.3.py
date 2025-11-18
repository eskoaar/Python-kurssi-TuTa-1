# 7.3
lentoasemat = {}


while True:
    print("\nvalitse vaihtoehto:")
    print("1 = kirjoita uusi lentokenttä")
    print("2 = lentokentän ICAO-koodi")
    print("0 = lopeta")


    valinta = input("kirjoita valintasi: ")

    if valinta == "1":
        icao = input("anna ICAO-koodi: ").upper()
        nimi = input("Aana lentokentän nimi: ")
        lentoasemat[icao] = nimi
        print("tallennettu.\n")

    elif valinta == "2":
        icao = input("anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"{icao} = {lentoasemat[icao]}")
        else:
            print("kyesitä koodia ei ole!.")

    elif valinta == "0":
        print("ohjelma päättyy.")
        break

    else:
        print("valintasi ei ole oikein.")
)