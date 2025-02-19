import re


def get(text):
    print(re.split(r"(?=[A-Z])", text))


get("iAmYourKing")  # iAmYourKing