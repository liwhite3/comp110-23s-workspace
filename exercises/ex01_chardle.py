"""EX01 - Chardle - A cute step toward Wordle."""
from typing import Counter

_author_ = "730506662"

# input pt.1
word: str = input("Enter a 5-character word: ")

# error pt.1
if (len(word)!=5):
    print("Error: Word must contain 5 characters")
    exit()

# input and error pt.2
letter: str = input("Enter a single character: ")
if (len(letter)!=1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)

# checking and index variables
if(letter == word[0]):
    print(letter + " found at index 0")
    if(letter == word[0]):
        A: int = 1
else:
        A: int = 0
if(letter == word[1]):
    print(letter + " found at index 1")
    if(letter == word[1]):
        B: int = 1
else:
        B: int = 0
if(letter == word[2]):
    print(letter + " found at index 2")
    if(letter == word[2]):
        C: int = 1
else:
        C: int = 0
if(letter == word[3]):
    print(letter + " found at index 3")
    if(letter == word[3]):
        D: int = 1
else:
        D: int = 0
if(letter == word[4]):
    print(letter + " found at index 4")
    if(letter == word[4]):
        E: int = 1
else:
        E: int = 0


# counting indices
indices = [A,B,C,D,E]

sum = sum(indices)
if(sum == 1):
    print("1 instance of " + letter + " found in " + word)
if(sum == 2):
    print("2 instances of " + letter + " found in " + word)
if(sum == 3):
    print("3 instances of " + letter + " found in " + word)
if(sum == 4):
    print("4 instances of " + letter + " found in " + word)
if(sum == 5):
    print("5 instances of " + letter + " found in " + word)