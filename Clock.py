import time
from datetime import datetime, timedelta
import keyboard

hour = None
able_print = True

##========= Afficher heure =========##
def afficher_heure(hour=None) :
    if hour==None : 
        actual_time = datetime.now()
        time = str(actual_time).split()[1].split('.')[0]
    else :
        str_time = hour[0] + ':' + hour[1] + ':' + hour[2]
        date_time = datetime.strptime(str_time, "%H:%M:%S")
        time = str(date_time + timedelta(seconds=1)).split()[1]
    if able_print :
        print(time)
    tuple_time = (time.split(':')[0], time.split(':')[1], time.split(':')[2])
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


keyboard.on_release_key('c', change_time)
running = True

##======== Mode 3 : Alarme ===========##
##if mode == '3' :
##    print('\n=============== ALARME =================')
##    h_alarm = input("Heure : ")
##    m_alarm = input("Minute : ")
##    s_alarm = input("Seconde : ")
##    alarm_time = (h_alarm, m_alarm, s_alarm)

##======== Mode 1 : Affichage de l'heure ==========##
while running :
    hour = afficher_heure(hour)
    change_time()
    ##alarm(alarm_time)
    time.sleep(1)
