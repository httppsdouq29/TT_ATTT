import random
def tim_s_r(n):
    s = 0
    r = n - 1
    while r % 2 == 0:
        r //= 2
        s += 1
    return s, r

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

def Miller_Rabin(n, t):
    s, r = tim_s_r(n)
    for _ in range(t):
        a= random.randint(2, n - 2)
        y = nhanbinhphuongcolap(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = (y * y) % n
                if y == 1:
                    return ("Hop so")
                j += 1
        if y != n - 1:
            return ("Hop so")
    return ("Nguyen to")

while True:
        try:
            n = int(input("Nhap n: "))
            if n <= 0:
                raise ValueError("Nhap lai n")
            break
        except ValueError as r:
            print(r)

try:
        t = int(input("Nhap so lan thu: "))
except ValueError:
        print("Hay nhap so nguyen")

result = Miller_Rabin(n, t)
if result == "Nguyen to":
    print(f"So {n} co kha nang la so nguyen to voi xac suat: {1 - 1/(4**t):.5f}")     
else:
     print(result)

