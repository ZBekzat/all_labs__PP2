import os

path = "."  # \Lab6\Part1
isExist = os.access(path, os.F_OK)  # мына путьты F_OK режимына тексеру
if not isExist:
    print("Current directory doesn't exist")
else:
    print("Checks if the path exists", isExist)
    print("Checks if the path is readable", os.access(path, os.R_OK))
    print(f"Checks if the path is writable {os.access(path, os.W_OK)}")
    print(f"Checks if the path is executable {os.access(path, os.X_OK)}")