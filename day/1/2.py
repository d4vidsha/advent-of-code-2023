from os.path import join, dirname, realpath


string_digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]


def first_last_digits(line: str) -> int:
    fst: str = ""
    for c in line:
        if c.isdigit():
            fst = c
            break
        else:
            fst += c
            for sd in string_digits:
                if sd in fst:
                    fst = str(string_digits.index(sd) + 1)
                    break
            if fst.isdigit():
                break

    lst: str = ""
    for c in reversed(line):
        if c.isdigit():
            lst = c
            break
        else:
            lst = c + lst
            for sd in string_digits:
                if sd in lst:
                    lst = str(string_digits.index(sd) + 1)
                    break
            if lst.isdigit():
                break

    return int(fst + lst)


def main():
    fp = open(join(dirname(realpath(__file__)), "input.txt"), 'r')
    lines = fp.readlines()
    fp.close()

    res = 0
    for i in range(len(lines)):
        res += first_last_digits(lines[i])
    return res


if __name__ == "__main__":
    print(main())