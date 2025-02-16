def getNumbers(n):
    for i in range(n, -1, -1):
        yield i


n = int(input("Enter n: "))
for i in getNumbers(n):
    print(i)