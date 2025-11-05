import random

def heita_noppaa():
    return random.randint(1, 6)


def paaohjelma_1():
    silma = 0
    while silma != 6:
        silma = heita_noppaa()
        print("Nopan heitto:", silma)