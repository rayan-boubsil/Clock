import time
from datetime import datetime, timedelta
import keyboard

##======= Init des variables globales =========##
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

    # gere le format am/pm
    if time_format == 24 :
        am_pm = ''
    elif time_format == 12 and int(time.split(':')[0])< 12 :
        am_pm = 'AM'
    elif time_format == 12 and int(time.split(':')[0]) >= 12 :
        am_pm = 'PM'

    print_time = (str(int(time.split(':')[0])%time_format).zfill(2), time.split(':')[1], time.split(':')[2])
    # gere le cas de midi
    if time.split(':')[0] == '12':
        print_time = ('12', print_time[1], print_time[2])
    # création du tuple de sortie
    tuple_time = (time.split(':')[0], time.split(':')[1], time.split(':')[2])

    ## Affichage heure
    if able_print :
        time_line = f'|              \033[91m{print_time[0]} : {print_time[1]} : {print_time[2]} {am_pm}\033[0m' + ' '*(15 - len(am_pm)) +'|'
        print (time_line)

    return tuple_time

##======== Réglage de l'heure ========##
def change_time(_event=None) :
    global able_print
    global hour
    if _event is not None :
        able_print = False
        print("\n\n\n========== REGLAGE DE L'HEURE ===========\n")
        new_h = input("Heure : ")
        new_m = input("Minute : ")
        new_s = input("Seconde : ")
        hour = (new_h, new_m, new_s)
        able_print = True
        return 0

##======== Pause ========##
def pause(_event=None):
    global paused
    if _event is not None:
        paused = not paused
        return 
    while paused:
        time.sleep(0.1)

##====== Alarme =======##

    # Réglage de l'alarme
def alarm(_event=None,) :
    if _event is not None :
        global alarm_time
        global able_print
        able_print = False
        print("\n========== REGLAGE DE L'ALARME ===========")
        h_alarm = input("Heure : ")
        m_alarm = input("Minute : ")
        s_alarm = input("Seconde : ")
        alarm_time = (str(int(h_alarm) % time_format).zfill(2), m_alarm.zfill(2), s_alarm.zfill(2))
        able_print = True

    # Vérification de l'alarme
def is_alarm(hour) :
    if hour ==  alarm_time and able_print:
        print("|_____________\033[94mC'EST L'HEURE !\033[0m______________|")
        return True
    elif able_print :
        print(f"|__________________________________________|")
        return False

##======= Changement de format de l'heure ========##
def switch_format(_event=None) :
    global time_format
    if _event is not None :
        if time_format == 24 :
            time_format = 12
        else :
            time_format = 24

##======= def des évenement clavier ========##
keyboard.on_release_key('c', change_time)
keyboard.on_release_key('p', pause)
keyboard.on_release_key('a', alarm)
keyboard.on_release_key('f', switch_format)

running = True

##======== Lancement de l'horloge ==========##
while running :
    if able_print :
        print('\n\n#==========================================#')
        print('|                                          |')
    hour = afficher_heure(hour)
    change_time()
    alarm()
    is_alarm(hour)
    if able_print :
        print('|\033[93mF\033[0m:format | \033[93mA\033[0m:alarme | \033[93mP\033[0m:pause | \033[93mC\033[0m:réglages|')
        print('#==========================================#')
    time.sleep(1)
    pause()