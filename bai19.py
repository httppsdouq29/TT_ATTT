import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def bieu_thuc(A, B, C, m, l):
    k = []
    for i  in range(m,l):
        val = A * pow(i,2) + B*i + C
        if is_prime(val):
            k.append(i)
    return k
        
while True:
    try:
        A = int(input("Nhập giá trị A: "))
        B = int(input("Nhập giá trị B: "))
        C = int(input("Nhập giá trị C: "))
        m = int(input("Nhập giá trị m: "))
        l = int(input("Nhập giá trị l: "))
        if m >= l:
            raise ValueError("Dãy số không hợp lệ")
        break
    except ValueError as z:
        print(z)

min_x = bieu_thuc(A, B, C, m, l)

print("Giá trị x sao cho Ax^2 + Bx + C là số nguyên tố:", min_x)