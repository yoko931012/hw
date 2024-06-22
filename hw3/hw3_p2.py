# input
poly = input("Input polynomial: ")
x = int(input("Input the value of X: "))

poly_ls = [s for s in poly]
i = 0

# combine numbers
while i+1 < len(poly_ls):
    if poly_ls[i].isdigit() and poly_ls[i+1].isdigit():
        poly_ls[i] = poly_ls[i] + poly_ls[i+1]
        del poly_ls[i+1]
        continue        
    i+=1

for i in range(len(poly_ls)):
    if poly_ls[i].isdigit():
        poly_ls[i] = int(poly_ls[i])
    
    if poly_ls[i] == "X":
        poly_ls[i] = x

# 第一位為負號
if poly_ls[0] == "-":
    poly_ls[1] = poly_ls[1]*-1
    del poly_ls[0]

# 處理 ^
i = 0
while i < len(poly_ls):
    if poly_ls[i] == "^":
        poly_ls[i] = poly_ls[i-1] ** poly_ls[i+1]
        del poly_ls[i+1]
        del poly_ls[i-1]
    i+=1

# 處理 *
i = 0
while i < len(poly_ls):
    if poly_ls[i] == "*":
        poly_ls[i] = poly_ls[i-1] * poly_ls[i+1]
        del poly_ls[i+1]
        del poly_ls[i-1]
    i+=1

# 處理 + -
i = 0
while i < len(poly_ls):
    if poly_ls[i] == "+":
        poly_ls[i] = poly_ls[i-1] + poly_ls[i+1]
        del poly_ls[i+1]
        del poly_ls[i-1]
        i=0
        continue

    if poly_ls[i] == "-":
        poly_ls[i] = poly_ls[i-1] - poly_ls[i+1]
        del poly_ls[i+1]
        del poly_ls[i-1]
        i=0
        continue
    i+=1

# output
print("Evaluated Result:", poly_ls[0])
