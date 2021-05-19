def calculator(a, b, state):
    if state == 'add':
        print(a+b)
    if state == 'minus':
        print(a-b)
    if state == 'mul':
        print(a*b)
    if state == 'div':
        print(a/b)

s = input('Please enter an action: ')

calculator(12, 19, s)
