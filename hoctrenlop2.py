def modula(a, k, n):
    return pow(a, k, n)

try:
    n = int(input("Nhập giá trị n: "))
    if n <= 1:
        raise ValueError("Giá trị của n phải lớn hơn 1.")

    a = int(input("Nhập giá trị a: "))
    k = int(input("Nhập giá trị k: "))

    if a >= n and k >= n:
        raise ValueError("Giá trị của a và k phải nhỏ hơn n.")

    result = modula(a, k, n)
    print(f"Kết quả của {a}^{k} mod {n} là: {result}")
except ValueError as e:
    print(e)
