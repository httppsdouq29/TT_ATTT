import math 

def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True 

def daynguyento(n):
    count = 0
    for i in range(1, n):
        if is_prime(i): 
            count +=1 
    return count
#trả về dãy có bao nhiêu số nguyên tố
def sieusonguyento(a , b):
    x = []
    for i in range(a , b + 1):
        if is_prime(daynguyento(i)) :
            x.append(i)
    return x
while True:
    try:
        a = int(input("Nhập giá trị A: "))
        b = int(input("Nhập giá trị B: "))
        if a > b :
            raise ValueError("Giá trị phải nhỏ hơn. Nhập lại.")
        break
    except ValueError as z:
        print(z)

result = sieusonguyento(a,b)

print("Các số siêu số nguyên tố là ", result)