import re

def get(text):
    matches = re.findall(r"[A-Z]+[a-z]+$", text)
    if len(matches) > 0:
        print(matches)
    else:
        print("not matches")

get("aVadakedavra")
get("Bratan")
get("Bro_SAMTYBRO")