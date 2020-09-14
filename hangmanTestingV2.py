theWord = "fair"

#if the user guesses letter "f",
# we would change the variable "theWord" to
# contain "air"

foundLetter = theWord.find("e")

if (foundLetter > -1):
    theWord = theWord[:foundLetter] + theWord[foundLetter+1:]

print(theWord)
