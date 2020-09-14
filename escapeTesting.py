print ("My nickname is \"Mike\"");

print("\tThis is indented")

print ("   O")
print ("   |")
print ("   |")
print ("  / \ ")
print ("=======")

word = "tree"

while (True):
    userInput = input("Please enter a guess:")

    if (word.find(userInput) == -1):
        print("Wrong guess")

    if (word.find(userInput) > -1 ):
        print("good guess")
