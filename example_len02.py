name01 = input('Please enter a name: ')
name02 = input('Please enter a name: ')
name03 = input('Please enter a name: ')

names = [name01, name02, name03]

for i in names:
    for x in i:
        if x == 'n':
            names.remove(i)
print(names)
