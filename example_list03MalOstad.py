animal_list = ['Cat', 'Dog']



s = 5

while s > 0:
    l = len(animal_list)
    input01 = input('Please enter a word: ')
    animal_list.insert(l, input01)
    s -= 1
print(animal_list)