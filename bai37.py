def compute_lps(S1):
    lps = [0] * len(S1)
    length = 0
    i = 1
    while i < len(S1):
        if S1[i] == S1[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(S1, S2):
    m = len(S1)
    n = len(S2)

    lps = compute_lps(S1)
    print("Bảng lps:", lps)

    i = 0
    j = 0
    while i < n:
        if S1[j] == S2[i]:
            i += 1
            j += 1
        if j == m:
            print(f"Mẫu xuất hiện tại chỉ số {i - j}")
            j = lps[j - 1]
        elif i < n and S1[j] != S2[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

if __name__ == "__main__":
    S1 = input("Nhập xâu mẫu S1: ")
    S2 = input("Nhập xâu văn bản S2: ")

    kmp_search(S1, S2)
