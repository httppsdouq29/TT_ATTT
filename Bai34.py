import random

def binary(number_k):
    k = []
    while number_k > 0:
        r = int(number_k % 2)
        k.append(r)
        number_k = number_k // 2
    k.reverse()
    return k


def squart_integer(number_a, number_k, number_n): #A^k mod n 
    k = binary(number_k)
    k.reverse()  # xét trọng số nho
    a = number_a
    if k[0] == 1:
        b = number_a
    else:
        b = 1
    for i in range(1, len(k)):
        a = (a * a) % number_n
        if k[i] == 1:
            b = (b * a) % number_n
    return b


def fermat(t, n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for _ in range(t): 
        a = random.randint(2, n - 2)
        if squart_integer(a, n - 1, n) != 1:
            return False
    return True


n = int(input('Nhập n = '))
t = int(input('Nhập t = '))
if fermat(t, n):
    print('Có thể là số nguyên tố')
else:
    print('Không phải là số nguyên tố')

    #sai khi trong các trường số carmichael, hay khi là các số giả nguyên tố Fermat đây là các số hợp số n mà a^n-1 = 1(mod n). khi với số lần k nhỏ dẫn đến kết quả sai 