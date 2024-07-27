import math

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def day_prime(n):
    k = []
    for i in range(2, n + 1):  
        if is_prime(i):
            k.append(i)
    return k
def haisonguyentosinhdoi(n):
    result = []
    for i in range(1, n):
        for j in range(1, n):
            if abs(i-j) == 2 :
                result.append((i,j))
    return result

while True:
    try:
        a = int(input("Nhập A: "))
        if a <= 0:
            raise ValueError("Giá trị phải là số nguyên dương. Nhập lại.")
        break
    except ValueError as z:
        print(z)

k = []
k = haisonguyentosinhdoi(a)

print(k)