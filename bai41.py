import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def nhanbinhphuongcolap(a, k, n):
    ds_k = []
    while k > 0:
        r = k % 2
        ds_k.append(r)
        k = int(k // 2)
    A = a
    if ds_k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(ds_k)):
        A = (A*A) % n 
        if ds_k[i] == 1:
            b = (A*b) % n
    return b

while True:
    try:
        a = int(input("Nhap a: "))
        if a <= 0 or a >= 1000:
            raise ValueError("Nhap lai a")
        break
    except ValueError as d:
        print(d)
while True:
    try:
        k = int(input("Nhap k: "))
        if k <= 0 or k >= 1000:
            raise ValueError("Nhap lai k")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        n = int(input("Nhap n: "))
        if n <= 0 or n >= 1000:
            raise ValueError("Nhap lai n")
        break
    except ValueError as f:
        print(f)

result = nhanbinhphuongcolap(a, k, n)
if ktnt(result):
    print(f"a^k mod n = {result} va {result} la so nguyen to")
else:
    print(f"a^k mod n = {result} nhung {result} khong la so nguyen to")
