import math


def main(x):
    arg1 = 54*pow(x, 4) + (pow(x, 2)/75)
    arg2 = pow((pow(x, 3)-25*x-pow(x, 2)), 4)-pow((pow(x, 2)-x-pow(x, 3)), 3)
    arg3 = 70*pow((11 + pow(x, 2)), 7) - 1
    arg4 = 18*math.log(x) + pow(x, 3)
    return arg1 / arg2 - arg3 / arg4


if __name__ == "__main__":
    print(main(0.4))
    print(main(0.41))
