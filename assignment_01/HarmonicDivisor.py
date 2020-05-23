import math


# Finds the total number of divisors and their sum  and then returns the harmonic mean of the divisors:
def FindDivisors(number):
    sum = 0
    length = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sum += 1/i
            length += 1
    # returning the harmonic mean:
    return length/sum


# Main function :
if __name__ == "__main__":
    count = 0
    for value in range(1, 10000):
        sum = FindDivisors(value)
    # checks if the result is an integer value :
        if round(sum, 8) - int(sum) == 0:
            print(value)
            count += 1
        if count == 10:
            break












