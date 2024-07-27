import math

def uoc(n):
    dem = 2
    for i in range(2, n):
        if (n % i == 0):
            dem = dem + 1
    return dem
def Q(n):
    a = []
    for i in range(1, n + 1):
        if (uoc(i) == 4):
            a.append(i)
    return a
n = int(input("Type N="))
print(Q(n))