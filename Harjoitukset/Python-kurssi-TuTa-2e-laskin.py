print("-----Tervetuloa käyttämään laskinta!-----")
print("Mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku \n D: Jakolasku")

valinta = input("Valintasi (A-D) ")

if valinta == "A":
    a = float(input("Anna ensimäinen luku: "))
    b = float(input("Anna toinen luku:"))
    print("Yhteenlasku")
elif valinta == "B":
    a = float(input("Anna ensimäinen luku: "))
    b = float(input("Anna toinen luku:"))
    print("vähennyslasku:", a - b)
elif valinta == "C":
    a = float(input("Anna ensimäinen luku: "))
    b = float(input("Anna toinen luku:"))
    print("kertolasku", a * b)
elif valinta == "D":
    a = float(input("Anna ensimäinen luku: "))
    b = float(input("Anna toinen luku:"))
    print("jakolasku:", a / b)
else:
    print("Valintasi oli virheellinen")
