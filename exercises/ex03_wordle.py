"""EX03 - Structured Wordle."""

__author__ = "730506662"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(guess: str, char: str) -> bool:
    """Determines if single character is found in user's guess and secret word"""
    assert len(char) == 1
    indx_var: int = 0
    while indx_var < len(guess):
        if guess[indx_var] == char:
            return True
        indx_var += 1
    return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Codifies the guess with colored boxes"""
    assert len (guess_word) == len (secret_word)
    result: str = ""
    indx_var: int = 0
    while indx_var < len(secret_word):
        if guess_word[indx_var] == secret_word[indx_var]:
            result += GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[indx_var]):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        indx_var += 1
    return(result)

def input_guess(expected_guess: int) -> str:
    """Determines proper length of users guess"""
    guess: str = input(f"Enter a {expected_guess} character word: ")
    while len(guess) != expected_guess:
        guess = input(f"That wasn't {expected_guess} chars! Try again: ")
        if len(guess) == expected_guess:
            return(guess)
    return(guess)
    
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess_number: int = 1
    has_not_won: bool = False
    while guess_number <= 6 and not has_not_won:
        print(f"=== Turn {guess_number}/6 ===")
        guess = input_guess(len(secret_word))
        result = emojified (guess, secret_word)
        print(result)
        if guess == secret_word:
            print(f"You won in {guess_number}/6 turns!")
            has_not_won = True
        guess_number += 1
        if guess_number == 7:
            print("X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()