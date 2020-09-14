#Mike McCue

#working with strings

theWord = "supercali"

#working with slices

#print(word[0:1]) # [from:to)

#word = word[0:1] + "-" + word[2:4]
#print(theWord[:1] + "-" + theWord[2:])

##
print(theWord.find("e"))

foundLetter = theWord.find("e")

print(theWord[:foundLetter] + "-" + theWord[foundLetter+1:])
