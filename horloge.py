import time 
import datetime
"""Module horloge.py"""

runnig=True
arlmeH=None
time_zone=None

def afficher_heure(time=None,time_zone=None):
    if  time_zone == 24:  
        if time is not None:
            actual_time = time
        else:
            t = datetime.datetime.now() 
            actual_time = (t.hour, t.minute, t.second)
        print(f'{actual_time[0]}:{actual_time[1]}:{actual_time[2]}')
        return actual_time
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
    
def alarme(time):
    global time_zone
    if time_zone==24:  
        if time[0]==arlmeH[0] and time[1]==arlmeH[1] and time[2]==arlmeH[2]:
            print("Il est l'heure !")
            global runnig
            runnig=False
    elif time_zone==12:                 
        if time[0]==arlmeH[0] and time[1]==arlmeH[1] and time[2]==arlmeH[2]:
            print("Il est l'heure !")
            global runnig
            runnig=False


while runnig:
    if time_zone is None:
        tz=input("Choisissez le format d'heure (12/24) : ")
        if tz!="12" and tz!="24":
            print("Format incorrect. Veuillez réessayer.")
            continue
        time_zone=int(tz)
    if arlmeH is None:
        arlmeh=input("Entrez l'heure de l'alarme (HH:MM:SS) : ")
        if len(arlmeh)!=8 or arlmeh[2]!=":" or arlmeh[5]!=":":
            print("Format incorrect. Veuillez réessayer.")
            continue
        arlmeh = (int(arlmeh[0:2]), int(arlmeh[3:5]), int(arlmeh[6:8]))
        arlmeH = arlmeh
    actual_time = afficher_heure(time_zone=time_zone)
    alarme(actual_time)
    time.sleep(1)        