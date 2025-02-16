def squares(a, b):
    for i in range(a, b + 1):
        yield pow(i, 2)


a, b = map(int, input().split())  # [1, 2]
for i in squares(a, b):
    print(i)