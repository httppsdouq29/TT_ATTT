import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def gcd(a, b): #x la nghich dao cua a mod b
    if b == 0:
        return a
    return gcd(b, a % b)
def nghich_dao(a, p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = v // u
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2, x1 = x1, x
    return (x1 + p) % p
while True:
    try: 
        p = int(input("Nhap SNT p: "))
        if ktnt(p) == False:
            raise ValueError("Nhap lai snt p")
        break
    except ValueError as z:
        print(z)
while True:
    try:
        a = int(input("Nhap a: "))
        if a<0:
            raise ValueError("Nhap lai a")
        break
    except ValueError as f:
        print(f)

if gcd(a, p) == 1:
    print(f"Nghich dao cua {a} la: {nghich_dao(a, p)}")
else: 
    print("Khong co nghich dao")



