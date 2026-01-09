import time
import threading

# Variable globale pour stocker l'alarme
alarme = None
alarme_lock = threading.Lock()  # verrou pour éviter les conflits

# Fonction pour régler l'alarme (appelée quand l'alarme sonne)
def set_alarm():
    global alarme
    while True:
        try:
            h = int(input("\nNouvelle alarme - Heure (0-23) : "))
            m = int(input("Minutes (0-59) : "))
            s = int(input("Secondes (0-59) : "))

            if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
                print("Heure invalide. Réessayez.")
                continue

            with alarme_lock:
                alarme = (h, m, s)
            print(f"Alarme réglée à {h:02}:{m:02}:{s:02}")
            break
        except ValueError:
            print("Entrée incorrecte. Réessayez.")

# Fonction pour afficher l'heure et gérer l'alarme
def show_time(heure):
    global alarme
    h, m, s = heure

    while True:
        print(f"{h:02}:{m:02}:{s:02}", end="\r", flush=True)

        with alarme_lock:
            if alarme is not None and (h, m, s) == alarme:
                print(f"\n L'alarme sonne ! Il est {h:02}:{m:02}:{s:02} !")
                alarme = None
                # Quand l'alarme sonne, demander une nouvelle alarme
                set_alarm()

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

# --- Programme principal ---
heure_depart = (20, 30, 0)

# Première alarme avant de lancer l'horloge
print("Réglez la première alarme :")
set_alarm()

# Lancement du thread pour l'horloge
thread_horloge = threading.Thread(target=show_time, args=(heure_depart,))
thread_horloge.daemon = True
thread_horloge.start()

# Garder le programme actif
thread_horloge.join()