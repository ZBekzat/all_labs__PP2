def getSquares(n):
    for i in range(1, n + 1):
        yield pow(i, 2)

n = int(input("Enter N: "))
for i in getSquares(n):
    print(i)