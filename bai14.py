import math

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def sodaonguoc(n):
    return int(str(n)[::-1])

def is_perfect_cube(n):
    cube_root = round(n**(1/3))
    return cube_root**3 == n               

def sum_prime():
    result = []
    for i in range (100, 1000):
        if is_prime(i):
            a = sodaonguoc(i)
            if is_perfect_cube(a):
                result.append(a)
    return result
special = sum_prime()
print("Các số nguyên tố có ba chữ số mà số đảo ngược là lập phương của một số tự nhiên là:")
print(special)