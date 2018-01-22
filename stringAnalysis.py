#James Roth
#1/22/18
#stringAnalysis.py - words and character counts

sentence=input("Enter a sentence ")
characters=int(len(sentence))
letters=int((characters-sentence.count(" ")))
#findchar=input("Enter a character to search for ")
print(letters)
print("Your sentence has", (sentence.count(" "))+1, "words and", characters, "characters and",)
#letters, "letters".)


