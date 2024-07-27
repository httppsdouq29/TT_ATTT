import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def super_prime(number_a, number_b):
    result_list = []
    for x in range(number_a, number_b + 1):
        count = 0
        for i in range(1, x):
            if is_prime(i):
                count += 1
        if is_prime(count):
            result_list.append(x)
    return result_list

while True:
    try:
        a = int(input("Nhập giá trị A: "))
        b = int(input("Nhập giá trị B: "))
        if a > b :
            raise ValueError("Giá trị phải nhỏ hơn. Nhập lại.")
        break
    except ValueError as z:
        print(z)

result = super_prime(a, b)
print(result)
print(f'Có {result} số siêu nguyên tố')