import re

text = "London 55 a5 is the capital Don don city of Great Britain"

match = re.findall(r"[^0-9][0-9]", text)
print(match)