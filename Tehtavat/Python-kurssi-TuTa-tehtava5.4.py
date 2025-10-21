kaupungit = []



for i in range(5):
    nimi = input(f"Mikä {i+1}. kaupunki: ")
    kaupungit.append(nimi)



print("Kaikki kaupungit:")
for nimi in kaupungit:
    print(nimi)
