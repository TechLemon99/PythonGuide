def methods():
    cap = str.capitalize("hello")
    case = str.casefold("HELLO")
    bb = str.count("hello", "l")
    ronen = str.endswith("hello", "o")
    raywing = str.index("hello", "e")
    return cap, case, bb, ronen, raywing

print(methods())