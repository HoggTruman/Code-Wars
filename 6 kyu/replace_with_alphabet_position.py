import re


def alphabet_position(text):
    text = re.sub(r"[^a-z]", "", text.lower())
    return " ".join(str(ord(l) - 96) for l in text)


print(alphabet_position("The sunset sets at twelve o' clock."))