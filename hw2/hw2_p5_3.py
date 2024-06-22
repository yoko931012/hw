# input
num = int(input("The number of the requested element in Fibonnacci (n) = " ))
s1 = input("The first string for Palindromic detection (s1) = ")
s2 = input("The second string for Palindromic detection (s2) = ")
plaintext = input("The plaintext to be encrypted: ")
print("----- extract key for encrypted method -----")

# Fibonacci sequence number
# initial values
f0 = 0
f1 = 1

i = 1
while i < num:
    tmp = f0
    # update f0 value to f1
    f0 = f1
    # f1 be the next number
    f1 = tmp + f1
    i += 1

print("The "+ str(num) +"-th Fibonacci sequence number is:", f1)

#LPS
#s1
l = len(s1)
pos = 0
# 回文的子序列
sub1 = ""
# 最長子序列為基數
while pos < l:
    # perceptron
    per = False
    # 以 position 為出發點，探查兩側字母是否一樣
    start = pos-1
    end = pos+1
    while start >= 0 and end < l:
        if s1[start] == s1[end]:
            # 出現一樣字母，顯示 True
            per = True
            if start-1 >= 0 and end+1 < l: 
                #分別向前後進行探查
                start -= 1
                end += 1
            else: 
                break
        else:
            # 當下一段文字不一樣，退回上一個一樣的地方，迴圈終止
            start += 1
            end -= 1
            break
    
    if per:
        new_sub = s1[start:end+1]
        # 如新發現的子序列長度比原本的長則取代
        if len(new_sub) > len(sub1):
            sub1 = new_sub
    pos += 1

pos=0
#最長子序列為偶數
while pos < l:
    per = False
    start = pos
    end = pos+1
    while end < l:
        if s1[start] == s1[end]:
            per = True
            if start-1 >= 0 and end+1 < l:
                start -= 1
                end += 1
            else:
                break
        else:
            start += 1
            end -= 1
            break
    if per:
        new_sub = s1[start:end+1]
        if len(new_sub) > len(sub1):
            sub1 = new_sub
    pos += 1

print("Longest palindrome substring within first string is:", sub1)
print("Length is:", len(sub1))

# s2
l = len(s2)
pos = 0
# 回文的子序列
sub2 = ""
# 最長子序列為基數
while pos < l:
    # perceptron
    per = False
    # 以 position 為出發點，探查兩側字母是否一樣
    start = pos-1
    end = pos+1
    while start >= 0 and end < l:
        if s2[start] == s2[end]:
            # 出現一樣字母，顯示 True
            per = True
            if start-1 >= 0 and end+1 < l: 
                #分別向前後進行探查
                start -= 1
                end += 1
            else: 
                break
        else:
            # 當下一段文字不一樣，退回上一個一樣的地方，迴圈終止
            start += 1
            end -= 1
            break
    
    if per:
        new_sub = s2[start:end+1]
        # 如新發現的子序列長度比原本的長則取代
        if len(new_sub) > len(sub2):
            sub2 = new_sub
    pos += 1

pos=0
#最長子序列為偶數
while pos < l:
    per = False
    start = pos
    end = pos+1
    while end < l:
        if s2[start] == s2[end]:
            per = True
            if start-1 >= 0 and end+1 < l:
                start -= 1
                end += 1
            else:
                break
        else:
            start += 1
            end -= 1
            break
    if per:
        new_sub = s2[start:end+1]
        if len(new_sub) > len(sub2):
            sub2 = new_sub
    pos += 1

print("Longest palindrome substring within second string is:", sub2)
print("Length is:", len(sub2))

print("----- encrypted completed -----")

# caesar  
key = f1
l_t = len(plaintext)

# tmp ciphertext
tmp_ci = ""

l = 0
while l < l_t:
    # current ciphertext
    cur_ci = chr((ord(plaintext[l])-65 + f1)%26 + 65)
    tmp_ci += cur_ci
    l += 1

# affine cipher
a = len(sub1)
b = len(sub2)
# final ciphertext
final_ci = ""

l = 0
while l < l_t:
    cur_a_ci = chr((ord(tmp_ci[l])*a + b-65) % 26 + 65)
    final_ci += cur_a_ci
    l += 1

print("The encrypted text is:", final_ci)