import math

def GCD(a, b): #thuật toán Eculid
    if b == 0:
        return a

    while b > 0:
        q = a // b
        r = a - q * b
        a = b
        b = r

    return a

def dap_an(m, n, d):
    result = []
    for i in range(m, n+1):
        for j in range(m, n+1):
            if GCD(i,j) == d:
                result.append((i,j))
    return result


while True:
    try:
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
        D = int(input("Nhập số D: "))

        if a > b or D > 1000 :
            raise ValueError("Không hợp lệ")
        break
    except ValueError as z:
        print(z)
ket_qua = dap_an(a, b, D)

print(ket_qua)