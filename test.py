import sys


def calc(a, b, op):
    calc = {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a / b,
}
    return calc[op]


def main(a, b, op):
    a = float(a)
    b = float(b)
    print(calc(a, b, op))


if __name__ == "__main__":
    params = sys.argv
    main(params[1], params[2], params[3])