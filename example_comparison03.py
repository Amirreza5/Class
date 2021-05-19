num = int(input('How many numbers do you want to compare: '))

list_num = list()

for i in range(0, num):
    inp_num = int(input('Please enter a number: '))
    list_num.append(inp_num)
list_num.sort()
print(list_num)


for x  in range(0, len(list_num)):
    for y in range(x, len(list_num)):
        if list_num[x] > list_num[y]:
            a_con = list_num[y]
            list_num[y] = list_num[x]
            list_num[x] = a_con


print(list_num)