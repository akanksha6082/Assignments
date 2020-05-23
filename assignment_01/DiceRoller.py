import random

if __name__ == "__main__":
    RollAgain = True
    while RollAgain:
        print("You are Rolling Dice!")
        print("Rolled Number : {0}".format(random.randint(1, 6)))
        print("Do you want to roll again - Enter Yes/No: ")
        RollAgain = ("y" or "yes") in input().lower()
    print("You Quit !")