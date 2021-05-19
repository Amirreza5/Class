from time import sleep

for A in range(101):
    sleep(0.2)

    if A % 5 != 0:
        print(A)
    elif A % 5 == 0 :
        print('hop')