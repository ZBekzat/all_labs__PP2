import re

def get(text):
    matches = re.sub(r"[ ,.]", ":", text)
    print(matches)

get("Hello world!,Bratan.")