def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r = r + 1 
        d = d // 2 

    def kiemtra(a, d, n, r):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = 2 + (hash((_, n)) % (n - 4))
        if kiemtra(a, d, n, r):
            return False

    return True

def timkiemsonguyentoN(n, k):
    start = 10**(n-1)
    end = 10**n - 1
    primes = []

    for number in range(start, end + 1):
        if miller_rabin(number, k):
            primes.append(number)

    return primes

N = int(input("Nhap so chu so  N: "))
k = 5  


primes = timkiemsonguyentoN(N, k)

# In kết quả
print(f"Các số nguyên tố có {N} chữ số là:")
for prime in primes:
    print(prime)
