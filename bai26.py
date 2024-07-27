import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def somanhme(n):
    k = []
    for x in range(n):
         for i in range(1, int(x/2) + 1):
             if is_prime(i) and x % i == 0 and x % (i * i) == 0:
                k.append(x)
    return k

while True:
    try:
        a = int(input("Nhập số a: "))
        if a > 1000 :
            raise ValueError("Không hợp lệ")
        break
    except ValueError as z:
        print(z)
ket_qua = somanhme(a)

print(ket_qua)