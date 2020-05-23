
def Input():
    while True:
        try:
            # taking input from the user
            a = int(input("Enter the value of a :"))
            r = int(input("Enter th value of r :"))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            break
    return a, r


if __name__ == "__main__":
    A, R = Input()
    if R == 0 or A == 0:
        print("0")
        exit()

    for i in range(0, 10):
        print(A*(R**i), end="\t")




