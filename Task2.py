import math


def main(x):
    if x < 11:
        return 3 * ((pow(x, 3)) - x) - pow(math.atan(66 * x), 6)
    if 11 <= x < 75:
        return 19 * pow(x, 5) + 5 * pow((38 * x - 39 * pow(x, 2)), 4)
    if x >= 75:
        return pow(x, 6)


if __name__ == "__main__":
    print("{:.2e}".format(main(154)))
    print("{:.2e}".format(main(-22)))
