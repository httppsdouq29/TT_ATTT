import math

def uoc(n):
    dem = 0
    for i in range(2, n):
        if (n % i == 0):
            dem = dem + 1 
    return dem
def T(n):
    a = []
    for i in range(1, n + 1):
        if (uoc(i) == 3):
            a.append(i)
    return a
n = int(input("Type N="))
print(T(n))