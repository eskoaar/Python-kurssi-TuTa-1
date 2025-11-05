import random

def heita_noppaa_tahkoilla(tahkoja):
    return random.randint(1, tahkoja)

def paaohjelma_2():
    maksimi = int(input("Kerro noppalukujen määrä: "))
    silma = 0
    while silma != maksimi:
        silma = heita_noppaa_tahkoilla(maksimi)
        print("Nopan heitto:", silma)
