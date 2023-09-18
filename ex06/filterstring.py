import sys
from ft_filter import ft_filter


def check_quote(s):
    """Check if the string contains punctuations"""
    return ft_filter(lambda x: x in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~", s)


def main():
    """main function"""
    try:
        assert len(sys.argv) == 3, "Two arguments only!!!"
        arr = check_quote(sys.argv[1])
        assert len(arr) == 0, "first argument must not contain punctuations"
        try:
            value = int(sys.argv[2])
            arr = ft_filter(lambda x: len(x) > value, sys.argv[1].split(" "))
            print(arr)
        except ValueError:
            assert False, "second argument is not an integer"
        return None
    except AssertionError as e:
        print("AssertionError: ", e)
        return None


if __name__ == "__main__":
    main()
