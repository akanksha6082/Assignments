import random


def GuessingNumber(number):
    while True:
        try:
            GuessedNumber = int(input("Guess any number: "))
        except ValueError:
            print("Enter the integer Value !")
        else:
            if GuessedNumber > number :
                print("Number is smaller than Guessed number")
            elif GuessedNumber < number:
                print("Number is greater than the Guessed number")
            else:
                print("You guessed the number right!")
                break


if __name__ == "__main__":
    GuessedNumber = random.randint(1, 100)
    GuessingNumber(GuessedNumber)