import re

# with open("input.txt", "r", encoding="utf-8") as file:
#     for i in range(len(file.readlines())):
#         if re.search(r"аб*", file.readline()):
#             print("FOUND!")
#         else:
#             print("NOT FOUND")

text = "abbbb ak ab erg"
matches = re.findall(r"ab+", text)
print(matches)
# if re.search(r"ab*", text):
#     print("FOUND")
# else:
#     print("NOT FOUND")