import random
def hopso(n, a=5):

    if n <= 1:
        return True
    if n <= 3:
        return False
    for _ in range(a):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return True
    return False


n = int(input("Nhập một số nguyên: "))
if hopso(n):
        print(f"{n} là hợp số.")

else:
        print(f"{n} có thể là số nguyên tố.")

