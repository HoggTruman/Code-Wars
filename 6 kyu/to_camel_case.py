import re


def to_camel_case(text):
    words = re.split(r"[_-]", text)
    return words[0] + "".join(w.title() for w in words[1:])


print(to_camel_case("the-stealth-warrior"))
