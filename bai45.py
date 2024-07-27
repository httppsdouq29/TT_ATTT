import random

def is_prime(n, k=5):  # số lần kiểm tra (độ chính xác cao hơn với số lớn hơn)
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime_array(N):
    prime_array = []
    candidate = 2  
    while len(prime_array) < N:
        if is_prime(candidate):
            prime_array.append(candidate)
        candidate += 1
    return prime_array

def min_distance(arr):
    arr.sort()
    min_dist = float('inf')
    for i in range(1, len(arr)):
        min_dist = min(min_dist, arr[i] - arr[i - 1])
    return min_dist

if __name__ == "__main__":
    N = int(input("Nhập số lượng phần tử N: "))
    prime_array = generate_prime_array(N)
    print("Mảng số nguyên tố:", prime_array)
    min_dist = min_distance(prime_array)
    print("Khoảng cách nhỏ nhất giữa 2 số bất kỳ trong mảng:", min_dist)
