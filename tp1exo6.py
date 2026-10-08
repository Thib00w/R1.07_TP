minutes = int(input("Indiquer nb minute depuis le debute du mois:\n>"))

heure = minutes//60
jour = heure//24

heure -= jour*24
minutes -= jour*24*60 + heure*60

print(f'La date du mois en cours est : {jour}j, {heure}h et {minutes}min')