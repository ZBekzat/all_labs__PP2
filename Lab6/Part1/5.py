import os

path = "."  # \Lab6\Part1
isExist = os.access(path, os.F_OK)  # мына путьты F_OK режимына тексеру
if not isExist:
    print("Current directory doesn't exist")
else:
    list = ["avadakedavra", "expect to patronum", "expilliarmus"]
    with open("file.txt", "w") as file:
        for i in list:
            file.write(i + "\n")