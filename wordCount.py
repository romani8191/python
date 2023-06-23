with open('resume','r') as file:
	data = file.read()
	lines = len(data.split())
print(f'number_of_words: {lines}')

