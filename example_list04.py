animal_list = ['Cat', 'Dog']

x = 5

while x > 0:
    input01 = input('Please enter a word: ')
    animal_list.append(input01)
    x -= 1
print(animal_list)