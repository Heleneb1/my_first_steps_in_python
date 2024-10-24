# On essaie de remplacer le b par m
word = "bonjour"
#word[0] = "m" TypeError: 'str' object does not support item assignment
print(word)
print(id(word))

print(word.replace('b','m'))
print(id(word.replace('b','m')))#Cette méthode ne modifie pas la chaîne word, elle en crée une nouvelle !

"monjour"

a = 'aze'
b = 'rty'
c = ''

print(a + b) # 'azerty'
print(a + c) # 'aze'

