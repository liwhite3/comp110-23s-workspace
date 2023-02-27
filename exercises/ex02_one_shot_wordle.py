"""EX02 - One Shot Wordle."""

__author__ = "730506662"

# gather inputs
secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
sum: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result: str = "" 


# check input len
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")


# checking indices
indx_var: int = 0

while indx_var < len(secret_word):
    if guess[indx_var] == secret_word[indx_var]:
        result += GREEN_BOX
    else:  # index of guess word != index of secret word
        chr_exist: bool = False
        alt_indx: int = 0
        while not chr_exist and alt_indx < len(secret_word): 
            if secret_word[alt_indx] == guess[indx_var]:
                chr_exist = True
            else:
                alt_indx += 1
        if chr_exist:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    indx_var += 1

print(result)

if guess != secret_word:
    print("Not quite. Play again soon ")
if guess == secret_word:
    print("Woo! You got it! ")
