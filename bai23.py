import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def prime(number_a, number_b):
    sum_k = 0
    for i in range(number_a, number_b + 1):
        if is_prime(i):
            sum_k += i
    return is_prime(sum_k)

while True:
    try:
        a = int(input("Nhập giá trị A: "))
        b = int(input("Nhập giá trị B: "))
        if a > b :
            raise ValueError("Giá trị phải nhỏ hơn. Nhập lại.")
        break
    except ValueError as z:
        print(z)

result = prime(a, b)
if result:
    print("Yes")
else:
    print("No")
   