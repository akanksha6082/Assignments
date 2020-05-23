def find_order(number):
    i = len(str(number))
    return i


if __name__ == "__main__":

    # take input from the user
    while True:
        try:
            LowerLimit = int(input("Enter lower range: "))
            UpperLimit = int(input("Enter upper range: "))
        except ValueError:
            print("Improper range ! Try again")
        else:
            break

    for num in range(LowerLimit, UpperLimit + 1):
        # initializing sum
        sum = 0
        # find the sum of the order of the digits
        temp = num
        i = find_order(num)
        while temp > 0:
            d = temp % 10
            sum += d ** i
            temp //= 10
        if num == sum:
            print(num)
