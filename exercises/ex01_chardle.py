"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730506662"

# input pt.1
word: str = input("Enter a 5-character word: ")
sum: int = 0
# error pt.1
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

# input and error pt.2
letter: str = input("Enter a single character: ")
if (len(letter) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)

# checking and index variables
if (letter == word[0]):
    print(letter + " found at index 0")
    sum = sum + 1
if (letter == word[1]):
    print(letter + " found at index 1")
    sum = sum + 1
if (letter == word[2]):
    print(letter + " found at index 2")
    sum = sum + 1
if (letter == word[3]):
    print(letter + " found at index 3")
    sum = sum + 1
if (letter == word[4]):
    print(letter + " found at index 4")
    sum = sum + 1


# counting indices
if sum == 0:
    print("No instances of " + letter + " found in " + word)
if sum == 1:
    print("1 instance of " + letter + " found in " + word)
if sum > 1:
    print(str(sum) + " instances of " + letter + " found in " + word)