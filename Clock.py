import time

running = True

while running :
    t = time.time()
    actual_time = time.ctime(t)
    just_time = actual_time.split()[3]
    print(just_time)
    time.sleep(1)
