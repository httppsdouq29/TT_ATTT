import math
import random


def soNguyenTo(n):  # hàm tính snt
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


def randomSoQ():  # random 2-500 khi nào  snt ngừng
    while True:
        q = random.randint(2, 500)  # 2 > q > 500
        if (soNguyenTo(q)):
            return q


def randomSoP():  # random chọn 100-500 ,khi nào được snt ngừng
    while True:
        p = random.randint(100, 500)  # 100 < p < 500
        if (soNguyenTo(p)):
            return p


def gcd(a, b):  # tìm ước chung ln
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def randomSoE(phi_n):
    while True:
        e = random.randint(2, phi_n)
        if gcd(e, phi_n) == 1:
            return e


def TinhD(a, b):  # tính nghịch đảo
    if b == 0:
        x = 1
        return x
    b1 = b
    x2 = 1
    x1 = 0
    while b > 0:
        q = int(a // b)
        r = a - q * b
        x = x2 - q * x1
        a = b
        b = r
        x2 = x1
        x1 = x
    x = x2
    return (x + b1) % b1


def BinhPhuongCoLap(number_a, number_k, number_n):
    k = []  # phân tích mũ k thành phị phân
    while number_k > 0:
        r = number_k % 2
        k.append(r)
        number_k = int(number_k // 2)
    a = number_a
    if k[0] == 1:  # nếu k [0] = 1 thì b = a ,và ngợc lại
        b = a
    else:
        b = 1
    for i in range(1, len(k)):
        a = int((a * a) % number_n)
        if k[i] == 1:
            b = int((b * a) % number_n)
    return b


q = randomSoQ()
p = randomSoP()
n = p * q
phi_n = (p - 1) * (q - 1)
e = randomSoE(phi_n)
d = TinhD(e, phi_n)
sbd = int(input("Nhập SBD = "))
print(f'D ={d} ')
m = sbd + 123
print(m)
c = BinhPhuongCoLap(m, e, n)  # bản mã
print(f'Bản mã c = {c}')
m = BinhPhuongCoLap(c, d, n)  # gải mã
print(f'Giải mã m= {m}')