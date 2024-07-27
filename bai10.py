import math 

def is_prime(n):
    if (a<=1):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(a % i == 0):
            return False
    return True 

def Uoc_so(n):
    dem = 0
    for i in range(2, n):
        if (n % i == 0):
            dem = dem + 1     
    return dem

def Uoc_so_NGTo(n):
    k = 0
    for i in range(2, n):
        if (n % i == 0) and (is_prime(i)) :
            k = k + 1     
    return k

a = int(input("Nhập vào số a = "))

Dem = Uoc_so(a)

Ngto = Uoc_so_NGTo(a)

print(Dem)
print(Ngto)