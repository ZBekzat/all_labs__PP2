import re


def get(text):
    matches = re.sub(r"_([a-z])", lambda l:l.group(1).upper(), text)
    print(matches)


get("i_am_your_king!")  # iAmYourKing