import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def result(number_a, number_b):
    sum = 0 
    for i in range(number_a, number_b):
        if is_prime(i):
            Fi = i
        else: 
            Fi = 0
        for j in range(i + 1 , number_b + 1):
            if is_prime(j):
                Fj = j
            else:
                Fj = 0
            sum += (Fi + Fj)
    return sum
        


while True:
    try:
        a = int(input("Nhập giá trị A: "))
        b = int(input("Nhập giá trị B: "))
        if a > b :
            raise ValueError("Giá trị phải nhỏ hơn. Nhập lại.")
        break
    except ValueError as z:
        print(z)

result_k = result(a, b)
print(result_k)
