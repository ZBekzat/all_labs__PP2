import functools

numbers = [1, 2, 3, 4, 5]
productOfNumbers = functools.reduce(lambda x, y: x * y, numbers)
print(productOfNumbers)
# prod = 1
# for i in numbers:
#     prod *= i
# print(prod)

# newNumbers = list(map(lambda x: x * 2, numbers)) # map(function, list)
# newFilteredNumbers = list(filter(lambda x: (x % 2 == 0), numbers))
# print(newNumbers)
# print(newFilteredNumbers)