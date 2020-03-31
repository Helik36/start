# слово -> СлОвО

word = 'слово'

result = []

for i in range(len(word)):
	# if i % 2 != 0: # всё это можно сделать как внзу
	# 	letter = word[i].lower()
	# else:
	# 	letter = word[i].upper()
		letter = word[i].lower() if i%2 !=0 else word[i].upper()
	result.append(letter)

result = ''.join(result)
print(result)