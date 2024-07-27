def extend_GCD(a, b):
    if b == 0:
        d = a
        x = 1
        y = 0
        return d, x, y

    x1, y1 = 0, 1
    x2, y2 = 1, 0
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2, x1 = x1, x
        y2, y1 = y1, y

    return a, x2, y2

try:
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))

        gcd, x, y = extend_GCD(a, b)

        print("GCD của a và b là", gcd)
        print("Hai hệ số x và y là", x, y)
except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")