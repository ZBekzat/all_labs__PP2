# try:
#     with open("file.txt", "r") as file:
#         lines = file.readlines()
#         print(lines)
#         print(len(lines))
# except FileNotFoundError:
#     print("Братан мундай файл жок")

with open("filebek.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    print(len(lines))