# calculates the sum of the divisors of the number:


def sumdivisors(number):
    sum = 1
    for i in range(2, number):
        if number % i == 0:
            sum += i
    return sum


# Main function
if __name__ == "__main__":
    count = 0
    i = 220
    while count <= 10:
        sum = sumdivisors(i)
        if sumdivisors(sum) == i and i != sum:
            # prints the amicable numbers in the field width of 4:
            print("{0:<4} and {1:<4}".format(i, sum))
            count += 1
            i = sum
        i += 1