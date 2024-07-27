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
    for i in range(2, n + 1):  # Bao gồm cả n
        if is_prime(i):
            k.append(i)
    return k

def sum_prime(n):
    a = day_prime(n)
    k = []
    for i in range(len(a)):  
        for j in range(i + 1, len(a)):  
            p1 = a[i]
            p2 = a[j]
            if is_prime(p1 + p2) and is_prime(abs(p1 - p2)):
                k.append((p1, p2))
    return k

while True:
    try:
        a = int(input("Nhập A: "))
        if a <= 0:
            raise ValueError("Giá trị phải là số nguyên dương. Nhập lại.")
        break
    except ValueError as z:
        print(z)

k = sum_prime(a)

if k:
    print("Các cặp số nguyên tố thỏa mãn điều kiện là:")
    for i in k:
        print(i)
else:
    print("Không có cặp số nguyên tố nào thỏa mãn điều kiện.")