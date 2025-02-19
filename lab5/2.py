import re

text = "abbbb ak abbb ab abb erg asd asd"
matches = re.findall(r"\bab{2,3}\b", text)
print(matches)