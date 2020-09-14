word = "fair"

#if the user guesses letter "f",
# we would change the variable "word" to
# contain "air"
foundIndex = 3
word = word[:foundIndex] + word[foundIndex+1:]

print(word)
