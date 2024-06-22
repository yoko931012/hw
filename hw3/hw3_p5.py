seats = input("Input sequence of seats: ").split()
seats = [int(ele) for ele in seats]
water = 0

# create right_maximum and left_maximum list
l_max = [0] * len(seats)
r_max = [0] * len(seats)

i = 0
while i < len(seats):
    j = i
    # right maximum
    while j < len(seats):
        if seats[j] >= seats[i] and seats[j] > r_max[i]:
            r_max[i] = seats[j]
        j+=1
    
    # left maximum
    j = i
    while j >= 0:
        if seats[j] >= seats[i] and seats[j] > l_max[i]:
            l_max[i] = seats[j]
        j-=1
    
    # calculate water
    # choose the smaller one between r_max and l_max
    water = water + min(r_max[i], l_max[i]) - seats[i]

    i+=1

print("Water:", water)
