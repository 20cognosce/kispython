def main(num):
    binary = bin(num)
    while len(binary) != 34:
        binary = binary[:2] + '0' + binary[2:]

    e = binary[2:5]
    d = binary[5:20]
    c = binary[20:26]
    b = binary[26:31]
    a = binary[31:34]

    a = int(a, 2) << 14
    b = int(b, 2) << 3
    c = int(c, 2) << 8
    d = int(d, 2) << 17
    e = int(e, 2)

    return a | b | c | d | e


if __name__ == "__main__":
    num1 = 4169311444
    num2 = 0xa430c128

    print(bin(num1))
    print(main(num1))


