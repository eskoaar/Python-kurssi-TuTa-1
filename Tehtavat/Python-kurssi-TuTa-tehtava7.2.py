nimet = set()


while True:
    nimi = input("kirjoita nimi: ").strip()

    if nimi == "":
        break

    if nimi in nimet:
        print("annetut nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)


print("\nannetut nimet:")
for n in sorted(nimet):
    print(n)
