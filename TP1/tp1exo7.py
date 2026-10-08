for i in range(3):
    x1 = int(input("Indiquer val x1:\n>"))
    x2 = int(input("Indiquer val x2:\n>"))
    x3 = int(input("Indiquer val x3:\n>"))
    conditions = [not(x1==x2) and not(x1==x2), (x1 > x2) or (x2 < x3), (x1<x2) and (x2<x3),
             not((x1>x2) and (x1<x3)), (x1 == x2) or (x3==x1) or (x2==x3)]
    if conditions[i]:
        print(f'condition est : {conditions[i]}')
    else:
        print(f'LA condition est : {conditions[i]}')
