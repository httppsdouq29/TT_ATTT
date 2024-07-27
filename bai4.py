import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def count_prime(a,b):
    dem = 0
    for i in range(a, b):
        if (is_prime(i)):
          dem+=1
    return dem

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

k = count_prime(a,b)
print("Số số nguyên tố nằm trong khoảng là",k)