# input the range
ran = int(input("Input the range number: "))
print("Perfect numbers: ")

for num in range(2, ran):
    # initialize the summation of the divisors
    sum = 0
    
    # d -> devisor
    for d in range(1, num):
        # test whether num can be divided by d
        if num % d == 0:
            sum += d
    
    if sum == num:
        print(num)