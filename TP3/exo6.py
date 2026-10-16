loop = True
while loop:
    try:
        heure_deb = int(input("Donnez l'heure de début de location (int): \n>"))
        heure_fin = int(input("Donnez l'heure de fin de location (int): \n>"))
        if heure_deb == heure_fin:
            print("L'heure de début est identique à l'heure de fin")
            raise ValueError
        if heure_fin < heure_deb: 
            print("L'heure de fin est avant l'heure de début")
            raise ValueError
        if not(1 <= heure_deb <= 24) or not(1 <= heure_fin <= 24): 
            print("L'heure doit etre compris entre 1 et 24")
            raise ValueError
        loop = False
    except:
        pass

somme = 0
i1 = 0
i2 = 0
while heure_deb != heure_fin:
    if 1 <= heure_deb <= 7 or 17 <= heure_deb <= 24:
        somme += 1
        i1 += 1
    else:
        somme += 2
        i2 += 1
    heure_deb += 1
print(f"Vous avez loué votre vélo pendant:\n - {i1} heure(s) au tarifs 1 euro(s)\n - {i2} heure(s) au tarifs 2 euro(s)\nLe monatnt total à ppayer est de {somme} euro(s)")

