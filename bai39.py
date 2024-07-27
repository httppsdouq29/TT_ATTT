import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def gcd(a, b):
    while b > 0:
        r = a % b
        a, b = b, r
    return a

while True:
    try: 
        n = int(input("Nhap so luong mang A: "))
        if n <=0:
            raise ValueError("Nhap lai")
        break
    except ValueError as z:
        print(z)

a = []
for i in range(1, n + 1):
    while True:
     try:
        temp = int(input(f"Nhap so nguyen duong thu {i}: "))
        if temp <= 0:
            raise ValueError("Hay nhap so nguyen duong!")
        break
     except ValueError as h:
         print(h)
    a.append(temp)
result = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if ktnt(gcd(a[i], a[j])):
            result.append((a[i], a[j]))
if result:
    print(f"Cac cap so trong mang A thoa man yeu cau la: {result}")
else:
    print("Khong co cap so thoa man yeu cau trong mang A")