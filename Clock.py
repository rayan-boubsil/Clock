import time
from datetime import datetime, timedelta


##========= Afficher heure =========##
def afficher_heure(hour=None) :
    if hour==None : 
        actual_time = datetime.now()
        time = str(actual_time).split()[1].split('.')[0]
    else :
        str_time = hour[0] + ':' + hour[1] + ':' + hour[2]
        date_time = datetime.strptime(str_time, "%H:%M:%S")
        time = str(date_time + timedelta(seconds=1)).split()[1]
    print(time)
    tuple_time = (time.split(':')[0], time.split(':')[1], time.split(':')[2])
    return tuple_time


hour = None
print("1 - Afficher l'heure\n2 - Régler l'heure\n3 - Ajouter une alarme")
mode = input("Saisire le num de l'action : ")

##======== Mode 3 : Alarme ===========##
if mode == '3' :
    print('\n=============== ALARME =================')
    h_alarm = input("Heure : ")
    m_alarm = input("Minute : ")
    s_alarm = input("Seconde : ")
    alarm_time = (h_alarm, m_alarm, s_alarm)

##======== Mode 2 : Réglage de l'heure ========##
if mode == '2' :
    print("\n========== REGLAGE DE L'HEURE ===========")
    h = input("Heure : ")
    m = input("Minute : ")
    s = input("Seconde : ")
    hour = (h, m, s)
    mode = '1'

##======== Mode 1 : Affichage de l'heure actuel ==========##
while mode == '1' :
    hour = afficher_heure(hour)
    ##alarm(alarm_time)
    time.sleep(1)
