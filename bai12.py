import math 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def day_prime(n):
    k = []
    for i in range(2, n):  # Bắt đầu từ 2 vì 0 và 1 không phải là số nguyên tố
        if is_prime(i):
            k.append(i)
    return k
    
def four_digit(n):
    k = day_prime(n)
    result = []
    for i in range(len(k) - 3):
        total = k[i] + k[i+1] + k[i+2] + k[i+3]  
        if total <= n and is_prime(total):
            result.append((k[i], k[i+1], k[i+2], k[i+3]))
    return result

n = int(input("Nhập số n: "))

prime_groups = four_digit(n)

print(prime_groups)
