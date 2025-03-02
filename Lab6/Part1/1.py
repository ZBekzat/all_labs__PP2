import os

path = "."
allElements = os.listdir(path)
print(allElements)
allDirs, allFiles = [], []
for el in allElements:
    if os.path.isdir(os.path.join(path, el)):
        allDirs.append(el)

for el in allElements:
    if os.path.isfile(os.path.join(path, el)):  # .1.py
        allFiles.append(el)

print("Directories", allDirs)
print("Files", allFiles)
print("All directories, files", allElements)