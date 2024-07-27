
import math


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            return False
    return True


def binary(number_k):
    k = []
    while number_k > 0:
        r = number_k % 2
        k.append(r)
        number_k = int(number_k // 2)
    k.reverse()
    return k


def square_integer(number_a, number_k, number_n):
    k = binary(number_k)
    k.reverse()
    a = number_a
    if k[0] == 1: # nếu k [0] = 1 thì b = a ,và ngược lại
        b = number_a
    else:
        b = 1
    for i in range(1, len(k)):
        q = int(a * a % number_n) # a=a^2 mod n
        a = q
        if k[i] == 1:
            b = int(b * q % number_n) #b= a.b mod n
    return b


def gcd(x, number_n):
    if number_n == 0:
        return x
    return gcd(number_n, x % number_n)


def check(i):
    for x in range(1, i):
        if gcd(x, i) == 1:
            if (square_integer(x, i - 1, i) != 1):  #ktra x^(i-1) mod i==1 tạm -> carmichael
                return False
    return True


def number_carmichael(number_n):
    for i in range(2, number_n):
        if is_prime(i) == False:
            if check(i):
                print(i, end=" ")


number_n = int(input('Nhập n = '))
number_carmichael(number_n)