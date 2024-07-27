import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def result(number_a, number_b, S1, S2):
    S = []
    for i in S1:
        for j in S2:
            sum = i + j
            if sum >= number_a and sum <= number_b and is_prime(sum) and sum not in S:
                S.append(sum)
    return S

while True:
    try:
        a = int(input("Nhập giá trị A: "))
        b = int(input("Nhập giá trị B: "))
        if a > b :
            raise ValueError("Giá trị phải nhỏ hơn. Nhập lại.")
        break
    except ValueError as z:
        print(z)



q = int(math.sqrt(b))

S1 = [x * x for x in range(1, q+1) ]

S2 = [x * x for x in range(1, q+1) ] 

result_K = result(a, b , S1, S2)

print(result_K)

   