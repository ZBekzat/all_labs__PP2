import re

def get(text):
    matches = re.findall(r"[a-z]+_[a-z]+$", text)
    if len(matches) > 0:
        print(matches)
    else:
        print("not matches")

get("avada_kedavra")
get("bratan")
get("bro_SAMTYBRO")
get("ok_ko")    