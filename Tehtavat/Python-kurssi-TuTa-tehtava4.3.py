luvut = []

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luvut.append(float(syote))

if luvut:
    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))
else:
    print("Et antanut lukua.")
