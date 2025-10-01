import random

oikea = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku 1–10: "))
    if arvaus < oikea:
        print("Liian pieni luku")
    elif arvaus > oikea:
        print("Liian suuri luku")
    else:
        print("Arvattu")
        break
