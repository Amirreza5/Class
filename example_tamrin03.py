from typing import Counter


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

input01 = input('Please enter a word: ')

list_numbers = len(alphabets)*['']
for i in range(0, len(alphabets)):
    list_numbers[i] = i

translated = len(input01)*[""]

for i in input01:
    c = 0
    for x in alphabets:
        if i  == x:
            translated.append(str(c))
        c += 1
    translated_final = ''.join(translated)
print(translated_final)