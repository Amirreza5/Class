Morse_code = { 'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
 'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
}
Text = input("please enter a word: ")
translate = ''
for character in Text:
    translate = Morse_code[character.upper()] + translate

print(translate)