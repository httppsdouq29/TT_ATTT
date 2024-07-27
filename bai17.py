import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def bieu_thuc(A, B, C):
    x = 1 
    while True:
        val = A * x**2 + B*x + C
        if is_prime(val):
            return x
        x += 1

while True:
    try:
        A = int(input("Nhập giá trị A: "))
        B = int(input("Nhập giá trị B: "))
        C = int(input("Nhập giá trị C: "))
        break
    except ValueError as z:
        print(z)

min_x = bieu_thuc(A, B, C)

print("Giá trị x nhỏ nhất sao cho Ax^2 + Bx + C là số nguyên tố:", min_x)