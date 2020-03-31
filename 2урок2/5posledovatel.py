friends_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guess', 'user')

if 'Max' in friends:
	print("У меня есть этот друг")

if 'M' in friends_name:
	print("Буква М есть в имени друга")

# for

for friend in friends: # тут friend создаёт  и по ней уже уже идёт отчёт
	print(friend)

for letter in friends_name:
	print(letter)

for role in roles:
	print(role)

print('end')

# while

# i = 0
# while i < len(friends):
# 	friend = friends[i]
# 	print(friend)
# 	i += 1