from os.path import join, dirname, realpath


def first_last_digits(line: str) -> int:
    fst: str
    for c in line:
        if c.isdigit():
            fst = c
            break
        
    lst: str
    for c in reversed(line):
        if c.isdigit():
            lst = c
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