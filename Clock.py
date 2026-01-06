import time
from datetime import datetime, timedelta
import keyboard

##======= Init des variable globales =========##
hour = None
able_print = True
paused=False
alarm_time = None
time_format = 24

##========= Afficher heure =========##
def afficher_heure(hour=None) :
    ## Heure actuelle si pas d'heure donnée
    if hour==None : 
        actual_time = datetime.now()
        time = str(actual_time).split()[1].split('.')[0]
    ## Ajoute 1 à l'heure donnée
    else :
        str_time = hour[0] + ':' + hour[1] + ':' + hour[2]
        date_time = datetime.strptime(str_time, "%H:%M:%S")
        time = str(date_time + timedelta(seconds=1)).split()[1]

    if time_format == 24 :
        am_pm = ''
    elif time_format == 12 and int(time.split(':')[0])<= 12 :
        am_pm = 'AM'
    elif time_format == 12 and int(time.split(':')[0]) > 12 :
        am_pm = 'PM'
    print_time = (str(int(time.split(':')[0])%time_format), time.split(':')[1], time.split(':')[2])
    tuple_time = (time.split(':')[0], time.split(':')[1], time.split(':')[2])

    ## Affichage heure
    if able_print :
        print('\n\n#==========================================#')
        print(f'\n                \033[91m{print_time[0]}:{print_time[1]}:{print_time[2]} {am_pm}\033[0m')
        if alarm_time!=None and alarm_time==tuple_time :
            print(" C'EST L'HEURE !")
        else : 
            print("")
        print(' \033[93mF\033[0m:format | \033[93mA\033[0m:alarme | \033[93mP\033[0m:pause | \033[93mC\033[0m:réglages')
        print('#==========================================#')
    return tuple_time

##======== Réglage de l'heure ========##
def change_time(_event=None) :
    global able_print
    global hour
    if _event is not None :
        able_print = False
        print("\n========== REGLAGE DE L'HEURE ===========")
        new_h = input("Heure : ")
        new_m = input("Minute : ")
        new_s = input("Seconde : ")
        hour = (new_h, new_m, new_s)
        able_print = True
        return True

##======== Pause ========##
def pause(_event=None):
    global paused
    if _event is not None:
        paused = not paused
        return 
    while paused:
        time.sleep(0.1)

##====== Alarme =======##
def alarm(_event=None) : 
    if _event is not None :
        global alarm_time
        global able_print
        able_print = False
        print("\n========== REGLAGE DE L'ALARME ===========")
        h_alarm = input("Heure : ")
        m_alarm = input("Minute : ")
        s_alarm = input("Seconde : ")
        alarm_time = (h_alarm, m_alarm, s_alarm)
        alarm_time = (str(int(alarm_time[0]) % time_format), alarm_time[1], alarm_time[2])
        able_print = True

##======= Changement de format de l'heure ========##
def change_format(_event=None) :
    global time_format
    global alarm_time
    if _event is not None :
        if time_format == 24 :
            time_format = 12
        else :
            time_format = 24
        if alarm_time is not None :
            alarm_time = (str(int(alarm_time[0]) % time_format), alarm_time[1], alarm_time[2])


##======= def des évenement clavier ========##
keyboard.on_release_key('c', change_time)
keyboard.on_release_key('p', pause)
keyboard.on_release_key('a', alarm)
keyboard.on_release_key('f', change_format)

running = True

##======== Lancement de l'horloge ==========##
while running :
    hour = afficher_heure(hour)
    change_time()
    alarm()
    time.sleep(1)
    pause()