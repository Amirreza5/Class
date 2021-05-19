number01 = int(input('Please write the first number: '))
number02 = int(input('Please write the second number: '))
number03 = int(input('Please write the third number: '))
number04 = int(input('Please write the fourth number: '))
number05 = int(input('Please write the fifth number: '))

numbers = [number01, number02, number03, number04, number05]

for i in numbers:
    if int(i) % 2 != 0:
        numbers.remove(str(i))
print(numbers)
