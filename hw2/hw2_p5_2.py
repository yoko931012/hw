# input
st = input("Enter a string: ")

# 輸入字串長度
l = len(st)
pos = 0
# 回文的子序列
sub = ""

# 最長子序列為奇數
while pos < l:
    # perceptron
    per = False
    # 以 position 為出發點，探查兩側字母是否一樣
    # start: 向前一格
    # end: 向後一格
    start = pos-1
    end = pos+1

    while start >= 0 and end < l:
        if st[start] == st[end]:
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
        new_sub = st[start:end+1]
        # 如新發現的子序列長度比原本的長則取代
        if len(new_sub) > len(sub):
            sub = new_sub
    pos += 1

pos=0

#最長子序列為偶數
while pos < l:
    per = False
    start = pos
    end = pos+1
    while end < l:
        if st[start] == st[end]:
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
        new_sub = st[start:end+1]
        if len(new_sub) > len(sub):
            sub = new_sub
    pos += 1

print("Longest palindrome substring is:", sub)
print("Length is: ", len(sub))