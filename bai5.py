import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def sum_prime(a,b):
    dem = 0
    for i in range(a, b):
        if (is_prime(i)):
          dem +=i
    return dem

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

k = sum_prime(a,b)
print("Tổng số nguyên tố nằm trong khoảng là",k)