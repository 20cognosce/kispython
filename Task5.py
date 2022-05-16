import math


def main(vector):
    n = len(vector)
    vector.insert(0, 0)  # because summing starts with i = 1
    temp_sum = 0
    for i in range(1, n+1):
        arg1 = pow(vector[n+1-math.ceil(i/3)], 3)
        arg2 = pow(vector[n+1-i], 2)
        temp_sum += 3 * pow((arg1 + arg2 + 60), 5)
    return temp_sum


if __name__ == "__main__":
    print("{:.2e}".format(main([-0.18, 0.12, -0.13, 0.26])))
    print("{:.2e}".format(main([0.78, -0.49, -0.15, -0.62])))

