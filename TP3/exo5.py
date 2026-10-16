def factfor(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

def factwhile(n):
    i = 1
    p = 1
    while i != n:
        p *= i
        i += 1
    return i

choice = None
loop = True
while loop:
    try:
        choice = input("Entrer while ou for pour votre choix :\n>")
        n = int(input("Donnez une valeur >0 :\n>"))
        if (choice == 'while' or choice == 'for') and n > 0:
            loop = False
        else:
            raise ValueError
    except:
        print("Valeur érroné...")
        pass

if choice == 'while':
    print(f"La factorielle de {n} est : {factwhile(n)}")
elif choice == 'for':
    print(f"La factorielle de {n} est : {factfor(n)}")
