from time import sleep

for x in range(100):
    sleep(0.2)

    if x % 2 == 0:
        print(x)
        print('Even')
    elif x % 2 != 0:
        print(x)
        print('Odd')
        
