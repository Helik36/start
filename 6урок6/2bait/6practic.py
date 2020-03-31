import json

favourite_tracks = [
	{'name': "Верная любовь", 'artist': 'Аганта Кристи'},
	{'name': "Angel", 'artist': 'Аганта massive Attack'},
	{'name': "Jamming", 'artist': 'Bob Marley'}
]

with open('track.json', 'w', encoding='utf-8') as f:
	json.dump(favourite_tracks, f)

print("записал")

