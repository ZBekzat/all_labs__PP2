def getEven(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
        continue


n = int(input("Enter n: "))
for san in getEven(n):
    if san == n or san - 1 == n:
        print(san)
    else:
        print(san, end=", ")