#bad character: Bảng này giúp xác định vị trí để dịch chuyển mẫu khi có ký tự không khớp.
#good suffix: Bảng này giúp xác định vị trí dịch chuyển khi có một phần của mẫu đã khớp.

def bad_character_table(S1):
    bad_char_table = {}
    length = len(S1)
    for i in range(length):
        bad_char_table[S1[i]] = length - i - 1
    return bad_char_table

def boyer_moore_search(S1, S2):
    m = len(S1)
    n = len(S2)

    bad_char_table = bad_character_table(S1)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and S1[j] == S2[s + j]:  #so sánh từ phải sang trái
            j -= 1
        if j < 0:
            print(f"Mẫu xuất hiện tại chỉ số {s}")
            s += m - bad_char_table.get(S2[s + m], m) if s + m < n else 1
        else:
            s += max(1, j - bad_char_table.get(S2[s + j], m))

if __name__ == "__main__":
    S1 = input("Nhập xâu mẫu S1: ")
    S2 = input("Nhập xâu văn bản S2: ")

    boyer_moore_search(S1, S2)



#Hiệu suất tốt hơn: Trong trường hợp trung bình, Boyer-Moore có thể bỏ qua nhiều ký tự hơn so với thuật toán tìm kiếm vét cạn, nhờ vào việc dịch chuyển theo bảng bad character và good suffix.
#Tối ưu cho mẫu dài: