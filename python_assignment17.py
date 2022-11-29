# Assignment 17
sentence = input("Please enter a sentence: ")
listed_sentence = list(sentence)
sentence_dictionary = {}
for letter in listed_sentence:
    sentence_dictionary[letter] = listed_sentence.count(letter)
print(sentence_dictionary)