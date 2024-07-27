import math
10
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def in_ra(a, dem):
    b = []
    for i in range( 1 , a):
        if (is_prime(i)):
            dem +=1
            b.append(i)
    return dem, b

a = int(input("Nhap so a: "))
dem = 0
k, so = in_ra(a,dem)

print(k,so)