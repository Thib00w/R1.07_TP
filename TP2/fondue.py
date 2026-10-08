BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nb_invite = int(input("Donnez le nb d'invité:\n>"))

fromage *= nb_invite/BASE
eau *= nb_invite/BASE
ail *= nb_invite/BASE
pain *= nb_invite/BASE

print(f"Pour faire une fandue fribourgeoise pour 3 personnes, il nous faut: \n- {fromage} gr de fromage\n- {eau} dL d'eau\n- {ail} gousses d'ail\n- {pain} gr de pain")