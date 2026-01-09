# Importation des bibliothèques
import time
import threading

# Variable globale pour stocker l'alarme
alarme = None

# Fonction pour régler l'alarme
def set_alarm():
    global alarme
    while True:
        try:
            h = int(input("\nHeure de l'alarme : "))
            m = int(input("Minutes : "))
            s = int(input("Secondes : "))
            alarme = (h, m, s)
            print(f"Alarme réglée à {h:02}:{m:02d}:{s:02d}")
        except ValueError:
            print("Entrée incorrecte, veuillez recommencer.")

# Fonction pour afficher l'heure
def show_time(heure):
    global alarme
    h, m, s = heure

    while True:
        print(f"{h:02d}:{m:02d}:{s:02d}", end="\r", flush=True)

        if alarme is not None and (h, m, s) == alarme:
            print("\n L'alarme sonne il est l'heure !")
            alarme = None

        time.sleep(1) 

        s += 1
        if s == 60:
            s = 0
            m += 1

        if m == 60:
            m = 0
            h += 1

        if h == 24:
            h = 0

# Lancement du programme
heure_depart = ((20, 30, 0))

# Thread qui permet d'éxécuter un petit programme en parallèle
thread_horloge = threading.Thread(target=show_time, args=(heure_depart,))
thread_horloge.daemon = True
thread_horloge.start()

set_alarm()