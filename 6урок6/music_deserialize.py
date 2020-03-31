import pickle, json

with open('group.pickle', 'rb') as f:
	group_bytes = pickle.load(f)
print(group_bytes)


with open('group.json', 'r', encoding='utf-8') as f:
	group_bytesj = json.load(f)
print(group_bytesj)
