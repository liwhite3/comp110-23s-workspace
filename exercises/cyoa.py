"""Choose your own adventure."""
# a buzzfeed quiz to determine your Hunger Games character


__author__ = "730506662"

import random
mylist = ["Cato", "Clove", "Enobaria", "Brutus"]
random_player = random.choice(mylist)

player: str = ""
points: int = 0
BAKER_EMOJI: str = '\U0001F9D1\u200D\U0001F373'
BRAIN_EMOJI: str = '\U0001F9E0'
BOW_AND_ARROW_EMOJI: str = '\U0001F3F9'


def greet() -> None:
    """Greeets the player."""
    global player
    print("Hello, and welcome to a buzzfeed quiz to determine your character in the Hunger Games and your district!")
    player = input("Enter your name: ")
    print(f"Welcome to the quiz {player} let's get started! ")


def main() -> None:
    """Runs the Hunger Games Personality Quiz."""
    global points
    playing: bool = True
    greet()
    while playing:
        choice: str = input("Type A, B, or C correlating to the following options. When confronted with a challenging situation do you... A: face it head on and tackle the problem, B: hide until the problem resolves itself, or C: throw bread at it ")
        if choice == "C":
            print(f"Congrats, now you don't have any bread and you're Peeta!{BAKER_EMOJI}")
            print(points)
            playing = False
        if choice == "B":
            points += 3
            # problem
            choice2()
        if choice == "A":
            points = choice3(points)
        

def choice2() -> None:
    """The Second Quiz Question For Those Who Chose 'B'."""
    global player
    global points
    choice: str = input(f"Nice choice {player}! Now, in your lucious amount of free time, would you rather, A: complete a sudoku puzzle, or B: read Nietzsche and contemplate capitalism. Hint: if you don't know who Nietzsche is, you should choose A.")
    if choice == "A":
        points += 3
        print(f"Congrats {player}, you are Beetee! {BRAIN_EMOJI}")
        print(f"You earned a total of {points} points!")
    if choice == "B":
        points += 5
        choice3(points)


def choice3(local_points: int) -> int:
    """Custom Int Function Run For Those Who Chose 'C'."""
    global player, random_player
    choice: str = input(f"Okay {player}, now finally, when you enter the Hunger Games arena and {random_player} is on your case, would you... A: eat some berries to get this nonesense over with, B: form an army of your peers to overthrow the capital, or C: play your hardest to eventually, one day, become the president of Panem ")
    if choice == "A":
        local_points += 0
    if choice == "B":
        local_points += 3
    if choice == "C":
        local_points += 5
        print(f"Congrats {player}, you are Katniss! {BOW_AND_ARROW_EMOJI}")
    return local_points


if __name__ == "__main__":
    main()