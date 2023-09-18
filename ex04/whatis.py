import sys

if len(sys.argv) == 2:
    try:
        value = int(sys.argv[1])
        if value % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2:
    print("AssertionError: More than one argument is provided")
