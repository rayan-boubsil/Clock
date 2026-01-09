import time
import threading

# Drapeau global pour contrôler l'affichage de l'horloge
afficher = True

def regler_alarme():
    global afficher
    afficher = False  # On stoppe l'affichage pendant la saisie

    print("\n--- Réglage de l'alarme ---")
    h = int(input("Heure de l'alarme (0-23) : "))
    m = int(input("Minute de l'alarme (0-59) : "))
    s = int(input("Seconde de l'alarme (0-59) : "))
    print(f"Nouvelle alarme réglée à {h:02d}:{m:02d}:{s:02d}\n")

    afficher = True  # On reprend l'affichage après la saisie
    return (h, m, s)

def verifier_alarme(h, m, s, alarmes):
    for i, alarme in enumerate(alarmes):
        if alarme is not None and (h, m, s) == alarme:
            print(f"\n Alarme ! Il est {h:02d}:{m:02d}:{s:02d} !")
            # Lancer un thread pour redemander une nouvelle alarme
            def nouvelle_alarme(i=i):
                alarmes[i] = regler_alarme()
            threading.Thread(target=nouvelle_alarme, daemon=True).start()

def afficher_heure(heure, alarmes):
    h, m, s = heure

    while True:
        # Affichage seulement si le drapeau est True
        if afficher:
            print(f"{h:02d}:{m:02d}:{s:02d}", end="\r", flush=True)

        time.sleep(1)

        # Ajouter 1 seconde
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0

        # Vérifier les alarmes
        verifier_alarme(h, m, s, alarmes)

# Liste d'alarmes (ici on gère juste une alarme)
alarmes = [regler_alarme()]
afficher_heure((20, 30, 0), alarmes)