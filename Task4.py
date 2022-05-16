import math


def main(n):
    if n == 0:
        return 0.46
    if n >= 1:
        arg1 = pow(0.02 + pow(main(n - 1), 2) / 46 + pow(main(n - 1), 3), 3)
        arg2 = pow(math.sin(main(n - 1)), 2)
        return 1 - arg1 - arg2


if __name__ == "__main__":
    print("{:.2e}".format(main(3)))
    print("{:.2e}".format(main(4)))
