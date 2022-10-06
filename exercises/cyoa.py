"""My C.Y.O.A. project!"""

__author__ = "730601447"

from random import randrange


points: int = 0
player: str = ""
sided_dice: int = 0
octopus: str = "\u1F419"
flower: str = "\ua9c1"

def main() -> None:
    """Entrypoint of program."""
    global points
    i: int = 0
    greet()
    while(i ==0):
        roll(sided_dice)
        print(f"{flower} Correct score: {points}")
        print(f"{flower} Would you like to play again, {player}? You have {points} points.")
        i = int(input("Type '0' for yes, type any other number for no: "))
        if(points < 3):
            quicktest: int = 0
            print("Your points are very low! Would you like to double or nothing on a coinflip?")
            quicktest = int(input("Type '0' for yes, type any other number for no: "))
            if(quicktest == 0):
                points = points + coinflip(points)
                print(f"{flower}Current points: {points}")
    print(f"{flower}Final correct score: {points} {octopus}")

    
def greet() -> None:
    """Greets the player and asks their name."""
    print(f"{flower}Welcome to the multi-sided dice game!")
    print(f"{flower}This is a game where you see how many times you can guess")
    print(f"{flower}a random number on a dice of side number of your choosing.")
    global player
    player = input("What is your name? ")
    global sided_dice
    sided_dice = int(input("How many sided dice would you like to play with, " + player + "? "))
    while sided_dice == 0:
        sided_dice = int(input("Can't have a 0 sided dice! How many sides, " + player + "? "))



def roll(sides: int) -> int:
    """Gets a roll from an n sided dice, and compares it to users guess."""
    i: int = 0
    roll: int = 0
    guess: int = 0
    global sided_dice
    global player
    while(i == 0):
        roll = randrange(sided_dice + 1)
        print(roll)
        guess = int(input("What is your guess for the roll, " + player + "? "))
        while(guess > sided_dice):
            guess = int(input("Too large of a guess! Try again: "))
        if(guess == roll):
            global points
            points = points + 1
        else:
            i = i + 1
    print(f"{flower}You guessed incorrectly, {player}!")

def coinflip(initialpts: int) -> int:
    """Flips a coin and sets player points to 0 or doubles them"""
    print(f"{flower}Flipping the coin!")
    if(randrange(2) == 1):
        print(f"{flower}You gambled correctly! Your score has been doubled!")
        return(initialpts)
    else:
        print(f"{flower}You gambled wrong! Your score has been set to 0.")
        return(-initialpts)

if __name__ == "__main__":
    main()