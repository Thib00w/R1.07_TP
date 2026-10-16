def a(n: int):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    print(s)
    return s

def b():
    rep = None
    while rep == "100":
        rep = input("Entrez une valeur :\n>")
    print("Vous êtes sortie de la boucle")

def c():
    lst_val = []
    nb_inf_10 = 0
    nb_sup_10 = 0
    nb_sup_15 = 0
    while len(lst_val) == 10:
        try:
            val = int(input(f"Choisisez la valeur {len(lst_val)+1} entre 0 et 20 :\n>"))
        except:
            print("Veuillez entrer un nombre entier...")
            pass
        if 0 <= val <= 20:
            lst_val.append(val)
        else:
            print("La valeur doit être compris entre 0 et 20 inclus...")
            pass
    for nb in lst_val:
        if nb < 10:
            nb_inf_10 += 1
        if nb >= 10:
            nb_sup_10 += 1
        if nb >= 15:
            nb_sup_15 += 1
    print(f"Le nombre de valeurs qui sont inférieur a 10 est: {nb_inf_10}\n"\
          f"Le nombre de valeurs qui sont supérieur ou egal a 10 est : {nb_sup_10}\n"\
          f"Le nombre de valeurs qui sont supérieur ou egal a 15 est : {nb_sup_15}")

def d():
    s = 0
    i = 0
    loop = True
    while loop:
        try:
            x = int(input("Donnez une valeur >1 :\n>"))
            if x > 1:
                loop = False
            else:
                raise ValueError
        except:
            print("La valeur doit être un nombre entier qui est >1 ....")
            pass
    while s < x:
        i += 1
        s += i
    print(f"Le plus grand nombre n est : {i}")
    return i