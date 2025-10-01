while True:
    tuuma = float(input("Anna tuumia: "))
    if tuuma < 0:
        print("Koodi lopetettu.")
        break
    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa = {c1m:.2f} cm")
