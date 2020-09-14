theWord = "fair"

#if the user guesses letter "f",
# we would change the variable "theWord" to
# contain "air"

userGuess = input("Enter a letter: ")
                  
while (len(theWord) > 0):
    foundLetter = theWord.find(userGuess)

    if (foundLetter > -1):
        theWord = theWord[:foundLetter] + theWord[foundLetter+1:]

    print(theWord)

    if (len(theWord) > 0):
        userGuess = input("enter a letter: ")

if (len(theWord) == 0):
    print("you guessed it")



