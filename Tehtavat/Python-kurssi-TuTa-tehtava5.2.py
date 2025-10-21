luvut = []



while True:
    syote = input("Syötä numero tai luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(int(syote))



luvut.sort(reverse=True)
print("Viisi suurinta numeroa tai lukua:", luvut[:5])
