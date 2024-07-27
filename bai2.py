import math

def uoc_so(a):
    k = []
    for i in range(1, a + 1):
        if a % i == 0:
            k.append(i)
    return k  

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def custom_sum(n):
    total = 0
    for i in n:
        total += i
    return total

n = int(input("Nhap so N = "))
a = uoc_so(n)
s = len(a)
prime_divisors = [i for i in a if is_prime(i)]
k = len(prime_divisors)
p = custom_sum(a)
q = custom_sum(prime_divisors)

tongso = n + p + s - q - k 

# Print the results
print(f"N = {n}")

print(f"Result (N + p + s - q - k) = {tongso}")
