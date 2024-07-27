import math
def is_prime(a):
    if (a<=1):
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if(a % i == 0):
            return False
    return True 

def sum_prime(n):
    tong = 0 
    for i in range(1, n):
        if (is_prime(i)):
            tong = tong + i
    return tong

while True:
    try:
        a = int(input("Nhập A:"))
        if a < 0 :
            raise ValueError("Nhập Lại")
        break
    except ValueError as z:
        print(z)

k = sum_prime(a)

print(k)