import re

def get(text):
    matches = re.findall(r"a.*?b$", text)
    if len(matches) > 0:
        print(matches)
    else:
        print("not matches")

get("aVadakedavra")
get("Brotanb")
get("Brao_SAMTYBROb")