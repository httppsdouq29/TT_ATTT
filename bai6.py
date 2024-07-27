import math

def sum_divisors(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i != n:
                cnt += i
            j = n // i
            if j != i and j != n:
                cnt += j
    return cnt

def friendly_math(a, b):
    return sum_divisors(a) == sum_divisors(b)

def search(n):
    k = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if friendly_math(i, j):
                k.append((i, j))
    return k

n = int(input("Nhập số n: "))

u = search(n)

print(u)
