import pickle as pickle
from random import choice

class markovChainDictionary:
	markovDictionary = {"":[]}
	words = []

	def __init__(self):
		try:
			self.markovDictionary = pickle.load(open("MarkovDump", "rb")) 
		except IOError:
			print("Could not load dictionary, empty dictionary created.\n")
			self.markovDictionary = {"": []}
		
	def addToDictionary(self,sentence):
		self.words = sentence.split(" ")

		self.markovDictionary[""].append(self.words[0])
		for index, word in enumerate(self.words):
			if not index == 0:
				self.markovDictionary[self.words[index-1]].append(word)
			if not word in self.markovDictionary:
				self.markovDictionary[word] = []
		self.markovDictionary[self.words[-1]].append("")

	def saveDictionary(self):
		pickle.dump(self.markovDictionary, open("MarkovDump", "wb"))

	def generateSentence(self):
		selectedWord = choice(self.markovDictionary[""])
		generatedSentence = selectedWord
		while selectedWord != "":
			selectedWord = choice(self.markovDictionary[selectedWord])
			generatedSentence = generatedSentence + " " + selectedWord

		return generatedSentence
		