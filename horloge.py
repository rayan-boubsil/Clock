import time 

t=time.time()
print(t)
actual_time=time.ctime(t)
print(actual_time)
just_time=actual_time.split()[3]
print(just_time)


def afficher_heure(time=None):
    if time is not None:
        just_time = time
    else:
        t = time
        actual_time = time.ctime(t)
        just_time = actual_time.split()[3]
    print(f"Heure : {just_time}")