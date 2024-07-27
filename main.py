import math
import re

p = 2147483647
W = 8
m = round(math.log2(p))
t = round(m / W)

def subtract(a, b, t):
    a.reverse()
    b.reverse()
    c = [0] * t

    borrow = 0
    for i in range(t):
        diff = a[i] - b[i] - borrow
        if diff < 0:
            diff += 256
        if a[i] < b[i] + borrow:
            borrow = 1
        else:
            borrow = 0
        c[i] = diff
    c.reverse()
    return c

def solve(a, W, p):
    result = []
    n = [pow(2, i * W) for i in range(t)]
    for i in n[::-1]:
        result.append(math.floor(a / i))
        a = a % i
    return result


def int_to_dec(n):
    n = bin(n)[2:].zfill(8 * t)
    b = re.findall('\d{8}', n)
    c = ['0b' + i for i in b]
    return [int(i, 2) for i in c]


def dec_to_int(n):
    n = ''.join([bin(i)[2:].zfill(8) for i in n])
    return int(n, 2)

def split_to_byte(n):
    binary_string = bin(n)[2:].zfill(16)
    byte1 = binary_string[-16:-8]
    byte2 = binary_string[-8:]
    num1 = int(byte1, 2)
    num2 = int(byte2, 2)
    return num1, num2

def multiprecision_addition(a, b, W, t):
    a.reverse()
    b.reverse()
    c = []
    epsilon = 0
    e = pow(2, 8)
    for i in range(t):
        s = a[i] + b[i] + epsilon
        x = s % e
        if s >= e:
            epsilon = 1
        else:
            epsilon = 0
        c.append(x)
    return [epsilon, c[::-1]]

def multiprecision_subtraction(a, b, W, t):
    a.reverse()
    b.reverse()
    c = []
    epsilon = 0
    e = pow(2, 8)
    for i in range(t):
        d = a[i] - b[i] - epsilon
        if d < 0:
            d += e
            epsilon = 1
        else:
            epsilon = 0
        x = d % e
        c.append(x)
    return epsilon, c[::-1]

def multiprecision_integer(a, b, t):

    a.reverse()
    b.reverse()

    c = [0] * (2 * t)

    for i in range(t):
        U = 0
        for j in range(t):

            d = c[i + j] + a[i] * b[j] + U
            U, V = split_to_byte(d)
            c[i + j] = V

        k = 1
        while U > 0:
            d = c[i + j + k - 1] + U
            U, V = split_to_byte(d)
            c[i + j + k - 1] = V
            k += 1

    return c[::-1]


def extend_GCD(a, b):
    if b == 0:
        d = a
        x = 1
        y = 0
        return d, x, y
    x1, y1 = 0, 1
    x2, y2 = 1, 0
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2, x1 = x1, x
        y2, y1 = y1, y
    return a, x2, y2


if __name__ == '__main__':

    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))


    h = solve(a, W, p)
    k = solve(b, W, p)
    print(h)
    print(k)
    print("Cong hai so nguyen",a+b)

    phep_tru = subtract(h,k,t)
    print("Tru hai so nguyen", phep_tru)

    [epsilon, c] = multiprecision_addition(h, k, W, t)

    p = int_to_dec(p)
    if epsilon == 1:
        l = multiprecision_subtraction(c, p, W, t)
    elif epsilon == 0:
        l = multiprecision_subtraction(p, c, W, t)
    print("Phep tru", l)

    if epsilon == 1:
        f = multiprecision_addition(c, p, W, t)
    elif epsilon == 0:
        f = c
    print("Phep Cong",f)

    result = multiprecision_integer(h, k, t)
    print("Phep Nhan",result)

