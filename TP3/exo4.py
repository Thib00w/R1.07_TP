import random as rnd

nb_random = rnd.randint(0,100)
loop = True
choice = None
while choice != nb_random:
    try:
        choice = int(input("Donnez une valeur compris entre 0 et 100 :\n>"))
        if not(0 <= choice <= 100):
            raise ValueError
        if choice < nb_random:
            print("La valeur est plus grande !")
        if choice > nb_random:
            print("La valeur est plus petite !")
        if choice == nb_random:
            print('Trouvé !!!') 
    except:
        print("La valeur doit être un nombre entier qui est entre 1 et 100....")
        pass