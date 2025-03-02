text = "Hello Bratan"
upperLetters = list(filter(lambda x: (x.isupper()), text))
lowerLetters = list(filter(lambda x: x.islower(), text))
print(upperLetters, len(upperLetters))
print(lowerLetters, len(lowerLetters))

lowers = sum(1 for i in text if i.islower())
uppers = sum(1 for i in text if i.isupper())
print(lowers)
print(uppers)