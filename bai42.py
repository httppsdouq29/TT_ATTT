import math, random
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def random_P():
    while True:
        p = random.randint(1, 999)
        if ktnt(p):
            return p
def random_Q():
    while True:
        q = random.randint(1, 999)
        if ktnt(q):
            return q
        
def nhanbinhphuongcolap(a, k, n):
    ds_k = []
    while k > 0:
        r = k % 2
        ds_k.append(r)
        k = int(k // 2)
    A = a
    if ds_k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(ds_k)):
        A = (A*A) % n 
        if ds_k[i] == 1:
            b = (A*b) % n
    return b

p = random_P()
q = random_Q()
if p == q:
    q = random_Q
g = []
for a in range(1, 100):
    if ktnt(nhanbinhphuongcolap(a, p ,q)):
        g.append(a)
print(g)