import time

def afficher_heure(heure):
    # On récupère les valeurs du tuple
    h = heure[0]
    m = heure[1]
    s = heure[2]

    # Boucle infinie pour afficher l'heure
    while True:
        print(f"{h:02d}:{m:02d}:{s:02d}", end="\r", flush=True)

        time.sleep(1)  # Attendre 1 seconde pour actualiser l'heure

        # On ajoute 1 seconde
        s = s + 1

        if s == 60:
            s = 0
            m = m + 1

        if m == 60:
            m = 0
            h = h + 1

        if h == 24:
            h = 0


# Affichage de l'heure avec des paramètres
afficher_heure((20, 30, 0))

