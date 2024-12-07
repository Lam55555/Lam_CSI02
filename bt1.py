chuoi = str(input("Nhap tu Tieng Anh: ")).lower()
def s_word(chuoi):
    word = chuoi.split()
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if len(word[i]) > len(word[j]):
                word[i], word[j] = word[j], word[i]
            elif len(word[i]) == len(word[j]):
                if word[i] > word[j]:
                    word[i], word[j] = word[j], word[i]
    return word
print(s_word(chuoi))