import math
import random

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def generate_random_array(size, lower_bound=1, upper_bound=1000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def find_primes_in_array(array):
    return [num for num in array if is_prime(num)]

while True:
    try:
        a = int(input("Nhập A: "))
        if a <= 0:
            raise ValueError("Giá trị phải là số nguyên dương. Nhập lại.")
        break
    except ValueError as z:
        print(z)

random_array = generate_random_array(a)

prime_numbers = find_primes_in_array(random_array)

print("Mảng ngẫu nhiên:", random_array)
print("Các số nguyên tố trong mảng:", prime_numbers)