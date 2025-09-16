alamitta = 37

pituus = int(input("Anna kuhan pituus sentteinä: "))

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen.")
    print(f"Kuha on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on riittävän suuri.")
