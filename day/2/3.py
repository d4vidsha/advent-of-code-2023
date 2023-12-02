from os.path import join, dirname, realpath


STATE = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def convert_to_state(s: str) -> dict:
    state = {}
    for token in s.split(","):
        (n, color) = tuple(token.strip().split(' '))
        state[color] = int(n)
    return state


def possible(subset: dict) -> bool:
    for color in subset:
        if subset[color] > STATE[color]:
            return False
    return True


def is_game_possible(game: str) -> int:

    (n, game) = tuple(game.split(':'))
    n = int(n.split(' ')[1])

    subsets = [subset.strip() for subset in game.split(';')]

    for subset in subsets:
        subset = convert_to_state(subset)
        if not possible(subset):
            return 0

    return n


def main():
    fp = open(join(dirname(realpath(__file__)), "input.txt"), 'r')
    lines = fp.readlines()
    fp.close()

    res = 0
    for i in range(len(lines)):
        res += is_game_possible(lines[i])
    return res


if __name__ == "__main__":
    print(main())
