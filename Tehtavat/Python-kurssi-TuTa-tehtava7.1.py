kuukausi = int(input("Kuukausi 1-12: "))


vuodenajat = {
    "kevät": [3, 4, 5],

    "kesä": [6, 7, 8],

    "syksy": [9, 10, 11],

    "talvi": [12, 1, 2]
}


for vuodenaika, kuukaudet in vuodenajat.items():
    if kuukausi in kuukaudet:
        print(f"vuodenaika {vuodenaika}.")
        break
