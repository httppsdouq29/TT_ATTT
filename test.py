def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes, is_prime

def count_super_primes(A, B):
    _, is_prime = sieve(B)
    primes_count = [0] * (B + 1)
    
    count = 0
    for i in range(1, B + 1):
        if is_prime[i]:
            count += 1
        primes_count[i] = count
    
    super_prime_count = 0
    for X in range(A, B + 1):
        if primes_count[X - 1] > 0 and is_prime[primes_count[X - 1]]:
            super_prime_count += 1
    
    return super_prime_count

# Đọc dữ liệu đầu vào từ bàn phím
A = int(input("Nhập A: "))
B = int(input("Nhập B: "))

# Tính và in ra kết quả
result = count_super_primes(A, B)
print(f"Số lượng siêu số nguyên tố trong khoảng [{A}, {B}] là: {result}")
