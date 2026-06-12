def methods():
    capitalize = str.capitalize("hello")
    casefold = str.casefold("HELLO")
    count = str.count("hello", "l")
    endswith = str.endswith("hello", "o")
    index = str.index("hello", "e")

    return capitalize, casefold, count, endswith, index

print(methods())