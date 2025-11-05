print("-----Tervetuloa käyttämään laskinta!-----")

while True:
    print("\n Mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku \n D: Jakolasku")

    valinta = input("Valintasi (A - D), Q lopettaa ()")

    #While loopin katkaisu
    if valinta == "Q":
        print("Ohjelma lopetetaan, kiitos hei!")
        break

    a = float(input("Anna ensimäinen luku: "))
    b = float(input("Anna toinen luku:"))

    if valinta == "A":
        print("Yhteenlasku", a + b)
    elif valinta == "B":
        print("vähennyslasku:", a - b)
    elif valinta == "C":
        print("kertolasku", a * b)
    elif valinta == "D":
        print("jakolasku:", a / b)
    else:
        print("Valintasi oli virheellinen")
