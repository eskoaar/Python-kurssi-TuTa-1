import random



n = int(input("Noppien lukumäärä: "))
summa = 0



for i in range(n):
    silmaluku = random.randint(1, 6)
    print(f"Nopan heitto: {i+1}: {silmaluku}")
    summa += silmaluku

print(f"Yhteistulos: {summa}.")
