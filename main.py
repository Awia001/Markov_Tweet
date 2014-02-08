from markov_test import markovChainDictionary

try:
	input = raw_input
except NameError:
	pass

dictionary = markovChainDictionary()
dictionary.addToDictionary(input("Input a sentence: "))
print(dictionary.generateSentence())
