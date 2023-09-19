import sys


def morse_code(s):
    """Convert string to morse code"""
    morse = {
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        " ": "/ "
    }
    str = ""
    for c in s:
        assert c.isalnum() or c.isspace(), "string must be alphanumeric"
        if c.upper() in morse:
            str += morse[c.upper()]
    print(str.strip())


def main():
    """main function"""
    try:
        assert len(sys.argv) == 2, "One arguments only!!!"
        morse_code(sys.argv[1])
    except AssertionError as e:
        print("AssertionError: ", e)
    return None


if __name__ == "__main__":
    main()
