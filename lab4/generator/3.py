def getDiv12(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i
        continue


n = int(input("Enter n: "))
for i in getDiv12(n):
    print(i)