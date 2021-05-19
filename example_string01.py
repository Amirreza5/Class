name = 'matin'
print(name.capitalize()) # the method return a string that its first letter is upper class
sentence01 = 'I like apples, because apples are delicious'

a = sentence01.split()
print(a)

b = ' '.join(a)
print(b)

c = 'matin'
d = c.upper() # d = MATIN
print(d)



e = d.lower()
print(e)

f = sentence01.count('apple')
print(f)