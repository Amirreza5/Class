num = int(input('How many numbers do you want to compare: '))

list_num = list()

for i in range(0, num):
    inp_num = int(input('Please enter a number: '))
    list_num.append(inp_num)
list_num.sort()
print(list_num)