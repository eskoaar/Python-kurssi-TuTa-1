Gallona_litroina = 3.785

def gallonat_litroiksi(gallonat):
    return gallonat * Gallona_litroina


def paaohjelma_3():
    while True:
        g = float(input("Gallonien määrä: "))
        if g < 0:
            break
        l = gallonat_litroiksi(g)
        print(f"{g} gallonaa = {l:.3f} litraa")

