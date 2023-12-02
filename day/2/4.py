from math import inf
from collections import defaultdict
from os.path import join, dirname, realpath


def convert_to_state(s: str) -> dict:
    state = {}
    for token in s.split(","):
        (n, color) = tuple(token.strip().split(' '))
        state[color] = int(n)
    return state


def power(game: str) -> int:

    (n, game) = tuple(game.split(':'))

    subsets = [convert_to_state(subset.strip()) for subset in game.split(';')]

    min_subset = defaultdict(int)

    for subset in subsets:
        for color in subset:
            if subset[color] > min_subset[color]:
                min_subset[color] = subset[color]

    pwr = 1
    for color in min_subset:
        pwr *= min_subset[color]

    return pwr


def main():
    fp = open(join(dirname(realpath(__file__)), "input.txt"), 'r')
    lines = fp.readlines()
    fp.close()

    res = 0
    for i in range(len(lines)):
        res += power(lines[i])
    return res


if __name__ == "__main__":
    print(main())
