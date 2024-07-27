import math, random
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def random_P():
    while True:
        p = random.randint(2, 99)
        if ktnt(p):
            return p
        
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

p = random_P()

while True:
    try:
        n = int(input("Nhap N: "))
        if n <= 0 or n >= 1000:
            raise ValueError("Nhap lai N!")
        break
    except ValueError as g:
        print(g)

A = []

for a in range(n):
    result = nhanbinhphuongcolap(a, p ,n)
    if ktnt(result):
        A.append(a)
if A:
    print("p = ", p)
    print(f"Cac so a < N thoa man a^{p} mod {n} la nguyen to la: {A}")
else:
    print("p = ", p)
    print("Khong co so a < {n} nao thoa man a^{p} mod {n} la so nguyen to")

