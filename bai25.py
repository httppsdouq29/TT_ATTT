# Cho 2 số M và N thoả mãn điều kiện: 1<=N<=10000; 2<M<=100; Hãy viết chương
# trình xác định xem số N có thể được phân tích thành tổng của M số nguyên tố hay không? Nếu
# có thì in ra các số đó.

def is_prime(num):
    """Kiểm tra số nguyên tố."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(limit):
    """Tìm tất cả các số nguyên tố nhỏ hơn hoặc bằng limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def find_sum_of_primes(primes, target, count): #target = N count = M
    """Tìm M số nguyên tố có tổng bằng N."""
    def backtrack(start, current_sum, path): # start = 0 , curSum= 0 , path = []
        if len(path) == count:
            if current_sum == target:
                return path
            return None # None là dừng lại nhánh này
        if current_sum > target or len(path) > count:
            return None

        for i in range(start, len(primes)):
            result = backtrack(i + 1, current_sum + primes[i], path + [primes[i]]) 
            #i + 1 làm vị trí bắt đầu mới (để không lặp lại số nguyên tố hiện tại).
            #Current_sum + primes[i] là tổng mới sau khi thêm số nguyên tố primes[i].
            #path + [primes[i]] là danh sách mới sau khi thêm số nguyên tố primes[i].
            if result:
                return result
        return None
    
    return backtrack(0, 0, [])

def main():
    N = int(input("Nhập N (1 <= N <= 10000): "))
    M = int(input("Nhập M (2 < M <= 100): "))
    
    if not (1 <= N <= 10000) or not (2 < M <= 100):
        print("Giá trị N hoặc M không hợp lệ.")
        return
    
    primes = find_primes(N)
    result = find_sum_of_primes(primes, N, M)
    
    if result:
        print(f"{N} có thể được phân tích thành tổng của {M} số nguyên tố: {result}")
    else:
        print(f"{N} không thể được phân tích thành tổng của {M} số nguyên tố.")

if __name__ == "__main__":
    main()
