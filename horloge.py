import time 
import datetime
import keyboard

"""Module horloge.py"""

runnig=True
arlmeH=None
time_zone=None
paused=False
modifier_alarme=False

def afficher_heure(time=None,time_zone=None):
    # Affiche l'heure actuelle au format  24h
    if  time_zone == 24:  
        if time is not None:
            actual_time = time
        else:
            # Obtenir l'heure et la date actuelle
            t = datetime.datetime.now() 
            # Extraire heures, minutes, secondes
            actual_time = (t.hour, t.minute, t.second)
        print(f'{actual_time[0]}:{actual_time[1]}:{actual_time[2]}')
        return actual_time  
    # Affiche l'heure actuelle au format 12h
    elif time_zone == 12:
        if time is not None:
            actual_time = time
        else:
            t = datetime.datetime.now() 
            hour = t.hour
            if hour > 12:
                hour -= 12
            actual_time = (hour, t.minute, t.second)
        print(f'{actual_time[0]}:{actual_time[1]}:{actual_time[2]} {t.strftime("%p")}')
        return actual_time
    
    
def pause(_event=None):
    global paused
    if _event is not None:
        paused = not paused
        return 
    while paused:
        time.sleep(0.1)
  
  
def alarme(time=None, _event=None):
    global arlmeH, modifier_alarme, runnig
    
    # Si appelé par hotkey 'r', time sera un KeyboardEvent
    if time is not None and hasattr(time, 'event_type'):
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
                arlmeH = arlmeh
            elif arlmeH is None and time_zone==12:
                arlmeh=input("Entrez l'heure de l'alarme (HH:MM:SS AM/PM) : ")
                if len(arlmeh)!=11 or arlmeh[2]!=":" or arlmeh[5]!=":" or arlmeh[8]!=" ":
                    print("Format incorrect. Veuillez réessayer.")
                    arlmeH=None
                    continue
                hour=int(arlmeh[0:2])
                if arlmeh[9:]=="PM" and hour!=12:
                    hour+=12
                elif arlmeh[9:]=="AM" and hour==12:
                    hour=0
                arlmeh = (hour, int(arlmeh[3:5]), int(arlmeh[6:8]))
                arlmeH = arlmeh
        return
    
    # Sinon, vérifier si l'alarme sonne
    if arlmeH is None:
        return
    if time_zone==24:  
        if time[0]==arlmeH[0] and time[1]==arlmeH[1] and time[2]==arlmeH[2]:
            print("Il est l'heure !")
            runnig=False
    elif time_zone==12:                 
        if time[0]==arlmeH[0] and time[1]==arlmeH[1] and time[2]==arlmeH[2]:
            print("Il est l'heure !")
            runnig=False


def main():
    global arlmeH
    global time_zone
    global modifier_alarme
    keyboard.on_release_key('p', pause)
    keyboard.on_release_key('r', alarme)
    while runnig:
        if time_zone is None:
            tz=input("Choisissez le format d'heure (12/24) : ")
            if tz!="12" and tz!="24":
                print("Format incorrect. Veuillez réessayer.")
                continue
            time_zone=int(tz)
        if arlmeH is None or modifier_alarme:
            modifier_alarme = False
            alarme()
        actual_time = afficher_heure(time_zone=time_zone)
        alarme(actual_time)
        time.sleep(1)
        pause()  
if __name__ == "__main__":
    main()        
      