import math

def SoNguyenTo(n):
    if n == 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def SoNhoHonMSV(msv):
    while True:
        if SoNguyenTo(msv):
            return msv
        msv -= 1


def SoLonHonMSV(msv):
    while True:
        if SoNguyenTo(msv):
            return msv
        msv += 1


def TimSoGanMSV(msv):  # tím số nguyên tố nhỏ ,lớn gần nhất vs msv
    soNho = SoNhoHonMSV(msv)
    soLon = SoLonHonMSV(msv + 1)
    if msv - soNho > soLon - msv:  # khoảng cách số nhỏ - msv lớn hơn số lớn -msv ,lấy số lớn
        return soLon
    else:
        return soNho  # nguwjojc lại


def BinhPhuongCoLap(number_a, number_k, number_n):
    k = []  # phân tích mũ k thành phị phân
    while number_k > 0:
        r = number_k % 2
        k.append(r)
        number_k = int(number_k // 2)  #các bit lần lượt từ phải sang trái
    
    a = number_a
    if k[0] == 1: # nếu k [0] = 1 thì b = a ,và ngợc lại
        b = a
    else:
        b = 1

    for i in range(1, len(k)):
        a = int((a * a) % number_n)  #Chuyển 2^i thành 2^2i
        if k[i] == 1:
            b = int((b * a) % number_n)  
    return b


a = int(input('SBD = '))
msv = int(input('MSV = '))
k = TimSoGanMSV(msv)
n = 123456
print(BinhPhuongCoLap(a, k, n))