import time

# On crée les variables 
h = 16
m = 30
s = 00

# Boucle infinie pour afficher l'heure
while True:
    print(f"{h:02d}:{m:02d}:{s:02d}", end="\r", flush=True)

# Attend 1 seconde pour actualiser
    time.sleep(1)

    # On ajoute 1 seconde
    s = s + 1
    # Si les secondes arrivent à 60 on ajoute 1 minute
    if s == 60: 
        s = 0
        m = m + 1
    # Si les minutes arrivent à 60 on ajoute 1 heure
    if m == 60:
        m = 0
        h = h + 1
    # Si les heures arrivent à 24 on revient à 0
    if h == 24:
        h = 0
