import math


def main(n, p, m):
    arg1 = 0
    arg3 = 0
    for j in range(1, n+1):
        arg1 += pow(j, 6)-pow((pow(j, 2) - 72 - p), 2) - pow((j+pow(p, 3)), 5)

    for j in range(1, n+1):
        arg2 = 0
        for k in range(1, m+1):
            arg2 += 45 * pow((pow(j, 3) - 94 - k), 6) + 28
        arg3 += arg2

    return arg1 - arg3


if __name__ == "__main__":
    print("{:.2e}".format(main(8, -0.68, 8)))
    print("{:.2e}".format(main(3, 0.77, 7)))
