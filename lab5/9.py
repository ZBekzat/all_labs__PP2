import re


def get(text):
    print(re.sub(r"([a-z])([A-Z])", r"\1 \2", text))


get("iAmYourKing")  # iAmYourKing