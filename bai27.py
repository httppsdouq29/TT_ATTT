import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def gcd(a, b):
    while b>0:
        r=a%b
        a=b
        b=r
    return a
def capsoNguyento(a, b):
    c = []
    for i in range(a+1, b):
        for j in range(a+1, b):
          if is_prime(gcd(i, j)):
            c.append({(i, j): gcd(i, j)})
    return c

while True:
    try:
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
        if  a <0 or a > 1000 or b < 0 or b > 1000 :
            raise ValueError("Không hợp lệ")
        break
    except ValueError as z:
        print(z)

result = capsoNguyento(a, b)
print(result)