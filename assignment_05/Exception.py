import sys
def inputno(prompt):

    while True:
        try:
            num1 = (int(input(prompt)))

        except(EOFError):
            print("\n End-of-file reached without reading any input, try again!")
        except(ValueError):
            print("Invalid Inputs please try again!")
        else:
            return num1

def division (num1, num2):
    try:
        result = num1/num2

    except(ZeroDivisionError):
        print("Number cannot be divided by zero")
        sys.exit(0)
    else:
        return result

if __name__ == "__main__" :

    num1 = inputno("enter first number : ")
    num2 = inputno("enter second number : ")

    print("{} divided by {} = {}".format(num1, num2, division(num1, num2)))

    arr = ["a", "b", "c", "d", "e", "f"]
    print(arr)

    while True:
        num1 = inputno("enter index number: ")
        try:
            print(arr[num1])
            break

        except (IndexError):
            print("invalid indexing of the array")





