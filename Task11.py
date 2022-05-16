from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1_size, offs = parse(buf, offs, 'uint16')
    a1_offs, offs = parse(buf, offs, 'uint32')
    a1 = []
    for _ in range(a1_size):
        val, a1_offs = parse_b(buf, a1_offs)
        a1.append(val)
    a2, offs = parse(buf, offs, 'uint64')
    a3, offs = parse(buf, offs, 'int16')
    a4, offs = parse_d(buf, offs)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'float')
    b2_size, offs = parse(buf, offs, 'uint32')
    b2_offs, offs = parse(buf, offs, 'uint16')
    b2 = []
    for _ in range(b2_size):
        val, b2_offs = parse(buf, b2_offs, 'char')
        b2.append(val.decode())
    b3, offs = parse(buf, offs, 'int16')
    b4, offs = parse(buf, offs, 'int8')
    b5_size, offs = parse(buf, offs, 'uint32')
    b5_offs, offs = parse(buf, offs, 'uint32')
    b5 = []
    for _ in range(b5_size):
        val, b5_offs = parse(buf, b5_offs, 'uint32')
        b5.append(val)
    b6, offs = parse(buf, offs, 'double')
    b7_offs, offs = parse(buf, offs, 'uint16')
    b7, b7_offs = parse_c(buf, b7_offs)
    return dict(B1=b1, B2=''.join(b2), B3=b3, B4=b4, B5=b5, B6=b6, B7=b7), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int8')
    c2, offs = parse(buf, offs, 'int32')
    c3, offs = parse(buf, offs, 'int32')
    return dict(C1=c1, C2=c2, C3=c3), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint8')
    d2 = []
    for _ in range(4):
        val, offs = parse(buf, offs, 'int16')
        d2.append(val)
    return dict(D1=d1, D2=d2), offs


def main(buf):
    return parse_a(buf, 4)[0]


encoded = (b'\xacRFU\x02\x00I\x00\x00\x00\xc9\xc2Y\xad\xc5;^}\x96\x11\x1f\xc6\x08\x0c'
           b'\x9dz\x14\r\rckykxlb\x0b\x06\xd5\xdcK\xa8N7}m(`\x92\x1b\x98\xc7\xbfakb'
           b'(\x10\x84\xf5\xdb\x1e\xedC\x00\x8e\xf2\xcb\x1e\xaa\xc6R \x01\xfd]'
           b'?\x07\x00\x00\x00\x1d\x00#\xd4c\x02\x00\x00\x00$\x00\x00\x00\x80\xf1'
           b'\xe8v\xdb\xb0\xa6?,\x00;\x91\xcc\xbe\x03\x00\x00\x005\x00\xbd\x17'
           b"\x1b\x02\x00\x00\x008\x00\x00\x00\xbc\xe3\x14\x11'\xa8\xd4?@\x00")

decoded = {'A1': [{'B1': 0.8671417832374573,
                   'B2': 'ckykxlb',
                   'B3': -11229,
                   'B4': 99,
                   'B5': [3704948235, 927901771],
                   'B6': 0.044318063989041256,
                   'B7': {'C1': 125, 'C2': -1839191955, 'C3': -1077438437}},
                  {'B1': -0.3995455205440521,
                   'B2': 'akb',
                   'B3': 6077,
                   'B4': 27,
                   'B5': [4119072808, 1139613403],
                   'B6': 0.3227632204830646,
                   'B7': {'C1': 0, 'C2': 516682382, 'C3': 542295722}}],
           'A2': 9033723622754730697,
           'A3': 4502,
           'A4': {'D1': 31, 'D2': [2246, -25332, 5242, 3341]}}
print(main(encoded))
print(decoded)
