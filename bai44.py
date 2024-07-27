import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

while True:
    try:
        n = int(input("Nhap so luong mang: "))
        if n<=0:
            raise ValueError("Nhap lai so luong")
        break
    except ValueError as g:
        print(g)
a = []
while True:
    try: 
        p = int(input("Nhap snt p: "))
        if not ktnt(p):
            raise ValueError("Nhap lai snt p")
        break
    except ValueError as z:
        print(z)
for i in range(1, n + 1):
    while True:
     try:
        temp = int(input(f"Nhap so nguyen duong thu {i}: "))
        if temp > p:
            temp = temp % p
        if temp <= 0 :
            temp = temp % p
            raise ValueError("Hay nhap so nguyen duong!")
        break
        
     except ValueError as h:
         print(h)
    a.append(temp)

B= [0 for _ in range(len(a))]

for i in range(len(a)):
    if gcd(a[i], p) == 1:
        B[i] = nghich_dao(a[i], p)
    else:
        B[i] = None
    
print(B)

