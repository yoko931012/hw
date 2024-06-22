# input
num = int(input("Input an integer number: "))

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