import math
import re


p = 2147483647
W = 8
m = round(math.log2(p))
t = round(m / W)

def solve(a, W, p):
    result = []
    n = [pow(2, i * W) for i in range(t)]
    for i in n[::-1]: #n[::-1] dùng để đảo ngược danh sách
        result.append(math.floor(a / i))
        a = a % i
    return result

def array_to_number(array, W):
    result = 0
    for i, value in enumerate(array[::-1]): #enumerate() cho phép bạn truy nhập vòng lặp lần lượt qua các thành phần của một collection trong khi nó vẫn giữ index của item hiện tại.
        result += value * pow(2, i * W)
    return result

def multiprecision_addition(a, b, W, t):
    a.reverse()
    b.reverse()
    c = []
    epsilon = 0
    e = pow(2, 8)
    for i in range(t):
        s = a[i] + b[i] + epsilon
        x = s % e
        if s >= e:
            epsilon = 1
        else:
            epsilon = 0
        c.append(x)
    return [epsilon, c[::-1]]

while True:
    try:
        a = int(input("Nhập giá trị A: "))
        b = int(input("Nhập giá trị B: "))
        break
    except ValueError as z:
        print(z)

h = solve(a, W, p)
k = solve(b, W, p)

[epsilon, c] = multiprecision_addition(h, k, W, t)

if epsilon == 1:
        f = multiprecision_addition(c, p, W, t)
elif epsilon == 0:
        f = c

result_number = array_to_number(f, W)

print("Kết quả dưới dạng mảng:", f)
print("Kết quả dưới dạng số:", result_number)