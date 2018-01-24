#James Roth
#1/22/18
#stringAnalysis.py - words and character counts

sentence=input("Enter a sentence: ")
characters=int(len(sentence))
letters=int((characters-sentence.count(" ")))
findchar=input("Enter a character to search for: ")
findword=input("Enter a word to search for: ")

print("Your sentence has", (sentence.count(" "))+1, "words and", characters, "characters and", letters, "letters.")
print("Your sentence has", sentence.count(findchar), "of the character", findchar, "and", sentence.count(findword), "of the word", findword + ".")