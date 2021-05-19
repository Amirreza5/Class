number01 = int(input('Please write the first number: '))
number02 = int(input('Please write the second number: '))
number03 = int(input('Please write the third number: '))
number04 = int(input('Please write the fourth number: '))
number05 = int(input('Please write the fifth number: '))

smallest = number01

if number02 < smallest:
    smallest = number02

if number03 < smallest:
    smallest = number03

if number04 < smallest:
    smallest = number04

if number05 < smallest:
    smallest = number05

print(smallest)