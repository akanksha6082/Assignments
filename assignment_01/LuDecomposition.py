
def LuDecompositon(Matrix, n):
    sum = 0
    Lower = [[0 for x in range(n)]
                for y in range(n)]
    Upper = [[0 for x in range(n)]
                for y in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                # this provides the sum of the product of the element from the lower and upeer triangular matrix resp.
                sum += Lower[i][j] * Upper[j][k]
            # for this the first row of the upper matrix is initialised to the first row of the matrix A :
            Upper[i][k] = Matrix[i][k] - sum

        for k in range(i, n):
            # Lower matrix's diagonal elements is initialised to 1
            if i == k:
                Lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += Lower[k][j] * Upper[j][i]
                Lower[k][i] = int((Matrix[k][i] - sum) / Upper[i][i])
    return Lower, Upper


if __name__ == "__main__":

    while True:
        try:
            n = int(input("Enter the number of the rows: "))
        except ValueError:
            print("Enter the Integer value")
        else:
            break

# Matrix Innput from the user:

Matrix = [[0 for x in range(n)]
             for y in range(n)]

print("Enter the Matrix data :")
for i in range(n):
    for j in range(n):
        while True:
            try:
                Matrix[i][j] = int(input())
            except ValueError:
                print("Enter only Integer values!")
            else:
                break

# printing the Matrix Data :
print("Matrix data :")
for i in range(n):
    for j in range(n):
        print(Matrix[i][j], end="\t")
    print()
Lower, Upper = LuDecompositon(Matrix, n)

# printing the Lower and  Upper triangular matrix:

print("Lower triangular Matrix :")
for i in range(n):
    for j in range(n):
        print(Lower[i][j], end="\t")
    print()

print("Upper triangular Matrix :")
for i in range(n):
    for j in range(n):
        print(Upper[i][j], end="\t")
    print()