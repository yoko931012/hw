# # 將單字轉換為 ASCII 碼
# ascii_list = [ord(c) for c in s]
# print(ascii_list)
# # 將 ASCII 碼套用公式
# new_ascii_list = [((num+x1)*len(s1[start:start+max_len])+len(s2[start:start+max_len])) for num in ascii_list]
# print(new_ascii_list)
# # 將新的 ASCII 碼轉換回單字
# new_word = ""
# for num in new_ascii_list:
#     if num < 65 or num > 90:
#         num = ((num - 65) % 26) + 65

#     else:
#         num=num
#     new_word += chr(num)



n = int(input())
for i in range(2, n+1):
    j=0
    for x in range(1, i+1):
        if i%x == 0:
            j=j+x
            if j/2 == i:
                print(i)