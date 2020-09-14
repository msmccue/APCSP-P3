theWord = "fair"

#if the user guesses letter "f",
# we would change the variable "theWord" to
# contain "air"

foundLetter = theWord.find("f")

if (foundLetter > -1):
    theWord = theWord[:foundLetter] + theWord[foundLetter+1:]

print(theWord)

if (len(theWord) == 0):
    print("you guessed it")


foundLetter = theWord.find("a")

if (foundLetter > -1):
    theWord = theWord[:foundLetter] + theWord[foundLetter+1:]

print(theWord)

if (len(theWord) == 0):
    print("you guessed it")

foundLetter = theWord.find("i")

if (foundLetter > -1):
    theWord = theWord[:foundLetter] + theWord[foundLetter+1:]

print(theWord)

if (len(theWord) == 0):
    print("you guessed it")

foundLetter = theWord.find("r")

if (foundLetter > -1):
    theWord = theWord[:foundLetter] + theWord[foundLetter+1:]

print(theWord)

if (len(theWord) == 0):
    print("you guessed it")
