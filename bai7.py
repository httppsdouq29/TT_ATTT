import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def emirp(n):
    reversed_n = 0
    while n > 0:
        # Lấy chữ số cuối cùng
        digit = n % 10
        
        # Ghép chữ số vào số ngược
        reversed_n = reversed_n * 10 + digit
        
        # Bỏ chữ số cuối cùng khỏi số ban đầu
        n = n // 10
    
    return reversed_n

def prin_emirp(n):
    k = []
    for i in range(1,n):
        if(is_prime(i)):
            dao_i = emirp(i)
            if is_prime(dao_i):
                k.append(i)
    return k

n = int(input("Nhap so n:"))

a = prin_emirp(n)

print(a)