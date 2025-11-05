def karsi_parittomat(luvut):
    return [l for l in luvut if l % 2 == 0]

def paaohjelma_5():
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = karsi_parittomat(luvut)
    print("Ensimmäinen:", luvut)
    print("Ei parittomia:", karsittu)