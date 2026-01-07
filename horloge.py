import time 
import datetime
import keyboard


# Variables globales
runnig=True
arlmeH=None
time_zone=None
paused=False
modifier_alarme=False
modif_heure=False
skip_next_display=False

def tick_time(time_tuple):
    h, m, s = time_tuple
    s += 1
    if s >= 60:
        s = 0
        m += 1
        if m >= 60:
            m = 0
            h += 1
            if h >= 24:
                h = 0
    return (h, m, s)

# Afficher l'heure actuelle (sans incrémenter)
def afficher_heure(time=None,time_zone=None):
    if time is None:
        # Obtenir l'heure et la date actuelle
        t = datetime.datetime.now() 
        actual_time = (t.hour, t.minute, t.second)
    else:
        # Afficher le temps fourni tel quel
        actual_time = time
    
    # Afficher selon le format
    if time_zone == 24:
        print(f'{actual_time[0]:02d}:{actual_time[1]:02d}:{actual_time[2]:02d}')
    elif time_zone == 12:
        hour = actual_time[0]
        ampm = "AM" if hour < 12 else "PM"
        if hour == 0:
            hour = 12
        elif hour > 12:
            hour -= 12
        print(f'{hour:02d}:{actual_time[1]:02d}:{actual_time[2]:02d} {ampm}')
    
    return actual_time
    
# Mettre en pause ou reprendre l'horloge
def pause(_event=None):
    global paused
    if _event is not None:
        paused = not paused
        return 
    while paused:
        time.sleep(0.1)
   
# Gérer l'alarme
def alarme(_event=None,time=None):
    global arlmeH, modifier_alarme, runnig
    
    # Si appelé par hotkey 'r', time sera un KeyboardEvent
    if _event is not None:
        modifier_alarme = True
        return   
    # Si time est None, c'est pour régler l'alarme
    if time is None:
        arlmeH=None
        while arlmeH is None:
            if arlmeH is None and time_zone==24:
                arlmeh=input("Entrez l'heure de l'alarme (HH:MM:SS) : ")
                if len(arlmeh)!=8 or arlmeh[2]!=":" or arlmeh[5]!=":":
                    print("Format incorrect. Veuillez réessayer.")
                    arlmeH=None
                    continue
                arlmeh = (int(arlmeh[0:2]), int(arlmeh[3:5]), int(arlmeh[6:8]))
                if arlmeh[0]>23 or arlmeh[1]>59 or arlmeh[2]>59:
                    print("Heure invalide pour le format 24h. Veuillez réessayer.")
                    arlmeH=None
                    continue
                arlmeH = arlmeh
            elif arlmeH is None and time_zone==12:
                arlmeh=input("Entrez l'heure de l'alarme (HH:MM:SS AM/PM) : ")
                if len(arlmeh)!=11 or arlmeh[2]!=":" or arlmeh[5]!=":" or arlmeh[8]!=" ":
                    print("Format incorrect. Veuillez réessayer.")
                    arlmeH=None
                    continue
                hour=int(arlmeh[0:2])
                if hour>12 or int(arlmeh[3:5])>59 or int(arlmeh[6:8])>59 or (arlmeh[9:]!="AM" and arlmeh[9:]!="PM"):
                    print("Heure invalide pour le format 12h. Veuillez réessayer.")
                    arlmeH=None
                    continue
                if arlmeh[9:]=="PM" and hour!=12:
                    hour+=12
                elif arlmeh[9:]=="AM" and hour==12:
                    hour=0
                arlmeh = (hour, int(arlmeh[3:5]), int(arlmeh[6:8]))
                arlmeH = arlmeh
        return   
    # Sinon, vérifier si l'alarme sonne
    if arlmeH and time_zone is not None:  
        if time[0]==arlmeH[0] and time[1]==arlmeH[1] and time[2]==arlmeH[2]:
            print("Il est l'heure !")
            runnig=False
            
def regler_heur(_event=None,time=None,time_zone=None):
    if _event is not None:
        global modif_heure
        modif_heure=True
        return
    Ntime=None    
    while Ntime is None:
            if time_zone==24:
                Ntime=input("Entrez la nouvelle heure (HH:MM:SS) : ")
                if len(Ntime)!=8 or Ntime[2]!=":" or Ntime[5]!=":":
                    print("Format incorrect. Veuillez réessayer.")
                    continue
                Ntime = (int(Ntime[0:2]), int(Ntime[3:5]), int(Ntime[6:8]))
                if Ntime[0]>23 or Ntime[1]>59 or Ntime[2]>59:
                    print("Heure invalide pour le format 24h. Veuillez réessayer.")
                    Ntime=None
                    continue
            elif time_zone==12:
                Ntime=input("Entrez la nouvelle heure (HH:MM:SS AM/PM) : ")
                if len(Ntime)!=11 or Ntime[2]!=":" or Ntime[5]!=":" or Ntime[8]!=" ":
                    print("Format incorrect. Veuillez réessayer.")
                    Ntime=None
                    continue
                hour=int(Ntime[0:2])
                if hour>12 or int(Ntime[3:5])>59 or int(Ntime[6:8])>59 or (Ntime[9:]!="AM" and Ntime[9:]!="PM"):
                    print("Heure invalide pour le format 12h. Veuillez réessayer.")
                    Ntime=None
                    continue
                if Ntime[9:]=="PM" and hour!=12:
                    hour+=12
                elif Ntime[9:]=="AM" and hour==12:
                    hour=0
                Ntime = (hour, int(Ntime[3:5]), int(Ntime[6:8]))
    if Ntime is not None:
        afficher_heure(time=Ntime, time_zone=time_zone)
        # Marquer pour ne pas réafficher dans la boucle suivante
        global skip_next_display
        skip_next_display = True
    return Ntime

def changer_format(_event=None):
    if _event is not None:    
        global time_zone
        if time_zone==24:
            time_zone=12
        else:
            time_zone=24



def main():
    global arlmeH
    global time_zone
    global modifier_alarme
    global modif_heure
    actual_time=None
    keyboard.on_release_key('p', pause)
    keyboard.on_release_key('r', alarme)
    keyboard.on_release_key('e', regler_heur)
    keyboard.on_release_key('f', changer_format)
    while runnig:
        if time_zone is None:
            tz=input("Choisissez le format d'heure (12/24) : ")
            if tz!="12" and tz!="24":
                print("Format incorrect. Veuillez réessayer.")
                continue
            time_zone=int(tz)
        # Traiter d'abord la demande de réglage d'heure pour afficher la valeur saisie
        if modif_heure:
            modif_heure=False
            actual_time=regler_heur(time_zone=time_zone)
        # Traiter une éventuelle demande d'alarme
        if  modifier_alarme:
            modifier_alarme = False
            alarme()
        # Afficher l'heure une seule fois par boucle
        global skip_next_display
        if skip_next_display:
            display_time = actual_time
            skip_next_display = False
        else:
            display_time = afficher_heure(time=actual_time, time_zone=time_zone)
        if arlmeH is not None: 
            alarme(time=display_time)
        # Incrémenter seulement si on a réglé manuellement l'heure
        if actual_time is not None:
            actual_time = tick_time(display_time)
        time.sleep(1)
        pause()
        changer_format()  
if __name__ == "__main__":
    main()        
      