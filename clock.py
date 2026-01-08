import time
from datetime import datetime, timedelta
import keyboard

##====== Initialisation des variables globales ======##
heure=None
pause=False
pouvoir_afficher=True
heure_alarme=None
heure_format=24

##====afficher heure=====##
def afficher_heure(heure=None):
    ## heure actuelle si pas fournie ##
    global pouvoir_afficher, heure_format
    if heure is None:
        heure_actuelle = datetime.now()
        heure = (heure_actuelle.hour, heure_actuelle.minute, heure_actuelle.second)
    ## Ajouter 1 a la seconde ##
    else: 
        heure_dt = datetime.now().replace(hour=heure[0], minute=heure[1], second=heure[2]) + timedelta(seconds=1)
        heure = (heure_dt.hour, heure_dt.minute, heure_dt.second)
    heure_aff = heure
        
    # Affichage selon le format choisi ##
    if heure_format==24:
        am_pm=""
    elif heure_format==12 and heure[0]>=12:
        am_pm=" PM"
        if heure[0]>12:
            heure_aff = (heure[0]-12, heure[1], heure[2])
    elif heure_format==12 and heure[0]<12:
        am_pm=" AM"
        if heure[0]==0:
            heure_aff = (12, heure[1], heure[2])
    #print_heure = f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}{am_pm}"
    ## Afficher l'heure ##
    if pouvoir_afficher:
        ligne_heure = f'|              \033[91m{heure_aff[0]:02d} : {heure_aff[1]:02d} : {heure_aff[2]:02d} {am_pm}\033[0m' + ' '*(15 - len(am_pm)) +'|'
        print(ligne_heure)

    return heure


#====== Réglage de l'heure ======##
def regler_heure(_event=None,heure_format=None):
    global heure, pouvoir_afficher
    reglage_en_cours=True
    if _event is not None:
        pouvoir_afficher=False
        print("\n===== Réglage de l'heure ====")
        while reglage_en_cours:
            nouvelle_heure = input("Entrez l'heure")
            nouvelle_minute = input("Entrez les minutes")
            nouvelle_seconde = input("Entrez les secondes")
            if heure_format==12:
                am_pm = input("AM ou PM ? ").strip().upper()
                if am_pm == "PM" and int(nouvelle_heure) < 12:
                    nouvelle_heure = str(int(nouvelle_heure) + 12)
                elif am_pm == "AM" and int(nouvelle_heure) == 12:
                    nouvelle_heure = "0"
            if (nouvelle_heure.isdigit() and 0 <= int(nouvelle_heure) < 24 and
                nouvelle_minute.isdigit() and 0 <= int(nouvelle_minute) < 60 and
                nouvelle_seconde.isdigit() and 0 <= int(nouvelle_seconde) < 60):
                heure = (int(nouvelle_heure), int(nouvelle_minute), int(nouvelle_seconde))
                reglage_en_cours = False
                pouvoir_afficher=True
            else:
                print("\n====Entrée invalide. Veuillez réessayer.=======")
        

##====Réglage de l'alarme=====##
def regler_alarme(_event=None,heure_format=None):
    global heure_alarme, pouvoir_afficher
    if _event is not None:
        reglage_en_cours=True
        pouvoir_afficher=False
        print("\n===== Réglage de l'alarme ====")
        while reglage_en_cours:
            nouvelle_heure = input("Entrez l'heure de l'alarme")
            nouvelle_minute = input("Entrez les minutes de l'alarme")
            nouvelle_seconde = input("Entrez les secondes de l'alarme")
            if heure_format==12:
                am_pm = input("AM ou PM ? ").strip().upper()
                if am_pm == "PM" and int(nouvelle_heure) < 12:
                    nouvelle_heure = str(int(nouvelle_heure) + 12)
                elif am_pm == "AM" and int(nouvelle_heure) == 12:
                    nouvelle_heure = "0"
            if (nouvelle_heure.isdigit() and 0 <= int(nouvelle_heure) < 24 and
                nouvelle_minute.isdigit() and 0 <= int(nouvelle_minute) < 60 and
                nouvelle_seconde.isdigit() and 0 <= int(nouvelle_seconde) < 60):
                heure_alarme = (int(nouvelle_heure), int(nouvelle_minute), int(nouvelle_seconde))
                reglage_en_cours = False
                pouvoir_afficher=True
            else:
                print("\n====Entrée invalide. Veuillez réessayer.=======")

def verifier_alarme(heure=None, heure_format=None):
    global heure_alarme, pouvoir_afficher
    if heure_alarme is not None and heure is not None:
        if heure == heure_alarme and pouvoir_afficher:
            pouvoir_afficher=True
            print("|  \33[92m===== ALARME ! ALARME ! ALARME ! =====\33[0m  |")
            heure_alarme = None  # Réinitialiser l'alarme après sonnerie
    elif pouvoir_afficher :
        print(f"|__________________________________________|")



##=====changer format heure====##
def changer_format(_event=None):
    global heure_format
    if _event is not None:
        if heure_format == 24:
            heure_format = 12
        else:
            heure_format = 24

##====pause====##
def pause_heure(_event=None):
    global pause, pouvoir_afficher
    if _event is not None:
        pause = not pause
        pouvoir_afficher = not pouvoir_afficher
        
###===== def des evenements clavier ======###
keyboard.on_press_key("f", changer_format)            
keyboard.on_press_key("a", regler_alarme)
keyboard.on_press_key("p", pause_heure)
keyboard.on_press_key("c", regler_heure)

###===== Boucle principale ======##
marche=True
while marche:
    if pouvoir_afficher :
        print('\n\n#==========================================#')
        print('|                                          |')
    heure=afficher_heure(heure)
    regler_heure(heure_format=heure_format)
    regler_alarme(heure_format=heure_format)
    verifier_alarme(heure=heure, heure_format=heure_format)
    if pouvoir_afficher :
        print('|\033[93mF\033[0m:format | \033[93mA\033[0m:alarme | \033[93mP\033[0m:pause | \033[93mC\033[0m:réglages|')
        print('#==========================================#')
    time.sleep(1)
    pause_heure()