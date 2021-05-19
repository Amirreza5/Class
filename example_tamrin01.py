number01 = int(input('Please write the first number: '))
number02 = int(input('Please write the second number: '))
number03 = int(input('Please write the third number: '))
number04 = int(input('Please write the fourth number: '))
number05 = int(input('Please write the fifth number: '))

smallest = number01
second_smallest = number01
third_smallest = number01

numbers = [number01 , number02 , number03 , number04 , number05]

for i in range (0, 6):
    if number02 < smallest:
        smallest = number02

    if number03 < smallest:
        smallest = number03

    if number04 < smallest:
        smallest = number04

    if number05 < smallest:
        smallest = number05
for i in range (0, 6):
    if number02 < second_smallest:
        second_smallest = number02

    if number03 < second_smallest:
        second_smallest = number03

    if number04 < smallest:
        second_smallest = number04

    if number05 < smallest:
        second_smallest = number05
    if smallest > second_smallest:
        smallest = second_smallest
for i in range (0, 6):
    if number02 < third_smallest:
        third_smallest = number02

    if number03 < third_smallest:
        third_smallest = number03

    if number04 < third_smallest:
        third_smallest = number04

    if number05 < third_smallest:
        third_smallest = number05
    if third_smallest < smallest or second_smallest:
        if second_smallest > smallest:
            third_smallest = second_smallest
        else:
            third_smallest = smallest
print(numbers)

