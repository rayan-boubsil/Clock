import time
from datetime import datetime, timedelta
import keyboard

##====== Initialisation des variables globales ======##
heure=None
pause=False
pouvoir_afficher=True
heure_alarme=None
heure_format=24
en_saisie=False
hotkeys_actifs = []  # Liste pour stocker les hotkeys actifs

##======= rafraichissement de l'heure ========#
def rafraichir_heure(heure=None) : 
    ## heure actuelle si pas fournie ##
    global pouvoir_afficher, heure_format
    if heure is None:
        heure_actuelle = datetime.now()
        heure = (heure_actuelle.hour, heure_actuelle.minute, heure_actuelle.second)
    ## Ajouter 1 a la seconde ##
    else: 
        heure_dt = datetime.now().replace(hour=heure[0], minute=heure[1], second=heure[2]) + timedelta(seconds=1)
        heure = (heure_dt.hour, heure_dt.minute, heure_dt.second)

    return heure

##==== afficher heure =====##
def afficher_heure(heure=None):
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
    ## Afficher l'heure ##
    if pouvoir_afficher:
        ligne_heure = f'|              \033[91m{heure_aff[0]:02d} : {heure_aff[1]:02d} : {heure_aff[2]:02d} {am_pm}\033[0m' + ' '*(15 - len(am_pm)) +'|'
        print(ligne_heure)

    return 0


#====== Réglage de l'heure ======##
def regler_heure():
    global heure, pouvoir_afficher, en_saisie, heure_format
    if not en_saisie:
        reglage_en_cours=True
        pouvoir_afficher=False
        en_saisie = True
        desactiver_hotkeys()
        print("\n===== Réglage de l'heure ====")
        while reglage_en_cours:
            nouvelle_heure = input("Entrez l'heure : ")
            nouvelle_minute = input("Entrez les minutes : ")
            nouvelle_seconde = input("Entrez les secondes : ")
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
            en_saisie = False
            reactiver_hotkeys()
        

##====Réglage de l'alarme=====##
def regler_alarme():
    global heure_alarme, pouvoir_afficher,heure_format, en_saisie
    if not en_saisie:
        reglage_en_cours=True
        pouvoir_afficher=False
        desactiver_hotkeys()
        en_saisie = True    
        print("\n===== Réglage de l'alarme ====")
        while reglage_en_cours:
            alarme_h = int(input("Entrez l'heure de l'alarme : "))
            alarme_m = int(input("Entrez les minutes de l'alarme : "))
            alarme_s = int(input("Entrez les secondes de l'alarme : "))
            if heure_format==12:
                am_pm = input("AM ou PM ? ").strip().upper()
                if am_pm == "PM":
                    alarme_h = alarme_h + 12
                elif am_pm == "AM" and alarme_h == 12:
                    alarme_h = "0"
                 # Vérifier que si heure > 12 et AM, c'est invalide
                if int(alarme_h) > 12 and am_pm == "AM":
                    print("\n====Entrée invalide. Veuiller réessayer .=======")
                    continue    
            if (str(alarme_h).isdigit() and 0 <= alarme_h < 24 and
                str(alarme_m).isdigit() and 0 <= alarme_m < 60 and
                str(alarme_s).isdigit() and 0 <= alarme_s < 60):
                heure_alarme = (alarme_h, alarme_m, alarme_s)
                reglage_en_cours = False
                pouvoir_afficher=True
            else:
                print("\n====Entrée invalide. Veuillez réessayer.=======")
        en_saisie = False
        reactiver_hotkeys()

def verifier_alarme(heure=None):
    global heure_alarme, pouvoir_afficher
    if heure_alarme is not None and heure is not None:
        if heure == heure_alarme and pouvoir_afficher:
            pouvoir_afficher=True
            print("|  \33[92m===== ALARME ! ALARME ! ALARME ! =====\33[0m  |")
            heure_alarme = None  # Réinitialiser l'alarme après sonnerie
            return 0
    if pouvoir_afficher :
        print(f"|__________________________________________|")



##=====changer format heure====##
def changer_format():
    global heure_format
    if not en_saisie:
        if heure_format == 24:
            heure_format = 12
        else:
            heure_format = 24

##====pause====##
def pause_heure():
    global pause, pouvoir_afficher, en_saisie   
    if not en_saisie:
        en_saisie=True
        desactiver_hotkeys()
        pause = not pause
        pouvoir_afficher = not pouvoir_afficher
        en_saisie=False
    reactiver_hotkeys()    
        
def desactiver_hotkeys():
    """Désactive tous les hotkeys"""
    global hotkeys_actifs
    for hk in hotkeys_actifs:
        keyboard.remove_hotkey(hk)
    hotkeys_actifs = []


def reactiver_hotkeys():
    """Réactive tous les hotkeys"""
    global hotkeys_actifs
    # D'abord s'assurer qu'ils sont bien désactivés
    desactiver_hotkeys()
    #time.sleep(0.2)
    # Puis les réactiver
    hotkeys_actifs.append(keyboard.add_hotkey('f', changer_format))
    hotkeys_actifs.append(keyboard.add_hotkey('a', regler_alarme ))
    hotkeys_actifs.append(keyboard.add_hotkey('p', pause_heure))
    hotkeys_actifs.append(keyboard.add_hotkey('c', regler_heure))
        
        
###===== Boucle principale ======##

reactiver_hotkeys()
marche=True
while marche:
    if pouvoir_afficher :
        print('\n\n#==========================================#')
        print('|                                          |')
    heure=rafraichir_heure(heure)
    afficher_heure(heure)
    verifier_alarme(heure=heure)
    if pouvoir_afficher :
        print('|\033[93mF\033[0m:format | \033[93mA\033[0m:alarme | \033[93mP\033[0m:pause | \033[93mC\033[0m:réglages|')
        print('#==========================================#')
    time.sleep(1)