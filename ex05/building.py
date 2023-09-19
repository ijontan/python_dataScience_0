import sys


def count_words(string: str):
    """count characters in string"""
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punctuation = 0

    for c in string:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        elif c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punctuation += 1

    print(f"text contains {len(string)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{digit} digits")
    print(f"{space} spaces")


def main():
    """main function"""
    if len(sys.argv) == 2:
        count_words(sys.argv[1])
    elif len(sys.argv) > 2:
        print("AssertionError: More than one argument is provided")
    else:
        line = sys.stdin.readline()
        count_words(line)
    return None


if __name__ == "__main__":
    main()
