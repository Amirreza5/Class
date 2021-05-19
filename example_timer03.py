from time import sleep 

second = 0
minute = 0
hour = 0

for x in range(1000000):
    sleep(0.1)
    print(hour, ':', minute, ':', second)
    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
