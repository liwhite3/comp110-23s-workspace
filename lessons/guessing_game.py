"""Ask for a number, until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing:
    if guess == SECRET:
        print("YAY! YOU GOT IT RIGHT.")
        playing = False
    else:
        print("Wrong number")
        if guess % 2 == 1: #guess is odd
            print("Guess should be even.")
        if guess > SECRET:
            print("your guess is too high")
        else: #guess is too low
            print("your guess is too low")
        guess = int(input("Make another guess "))