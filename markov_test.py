markovDictionary = {"": []}

sentence = raw_input("Input a sentence:\n")
words = sentence.split(" ")
print(words)

markovDictionary[""].append(words[0])
for index, word in enumerate(words):
	if not index == 0:
		markovDictionary[words[index-1]].append(word)
	if not markovDictionary.has_key(word):
		markovDictionary[word] = []
markovDictionary[words[-1]].append("")
		
	
print(markovDictionary.items())