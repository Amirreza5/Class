name01 = input('Please enter a name: ')
name02 = input('Please enter a name: ')
name03 = input('Please enter a name: ')
name04 = input('Please enter a name: ')
name05 = input('Please enter a name: ')
name06 = input('Please enter a name: ')
name07 = input('Please enter a name: ')

names = [name01, name02, name03, name04, name05, name06, name07]

for i in names:
    if len(i) >= 7:
        names.remove(i)
print(names)