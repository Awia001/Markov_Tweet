import pickle
from random import choice

try:
	markovDictionary = pickle.load(open("MarkovDump", "rb")) 
except IOError:
	markovDictionary = {"": []}
	
sentence = raw_input("Input a sentence:\n")
words = sentence.split(" ")
#print(words)

markovDictionary[""].append(words[0])
for index, word in enumerate(words):
	if not index == 0:
		markovDictionary[words[index-1]].append(word)
	if not markovDictionary.has_key(word):
		markovDictionary[word] = []
markovDictionary[words[-1]].append("")

pickle.dump(markovDictionary, open("MarkovDump", "wb"))

generatedSentence = ""
selectedWord = choice(markovDictionary[""])
generatedSentence = generatedSentence + " " + selectedWord
while selectedWord != "":
	selectedWord = choice(markovDictionary[selectedWord])
	generatedSentence = generatedSentence + " " + selectedWord

print(generatedSentence)
#print(markovDictionary.items())