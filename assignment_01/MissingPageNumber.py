# Input form the user

if __name__ == "__main__":
    RangeSet = input("Enter the range for book with 25 pages: ")
    List = []
    Range = []
    List = RangeSet.split(",")
    for value in List:
        if "-" in value:
            a, b = value.split("-")
            c = int(a)
            d = int(b)
            # Expansion of the ranges from thr input range for example : 4-10 into 4,5,6,7,8,9,10 :
            while c <= d:
                Range.append(c)
                c += 1
                
    for i in range(1, 26):
        if str(i) not in List and i not in Range:
            print(i, end="\t")
