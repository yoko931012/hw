# input
n = int(input("Input the total number of students (n>0): "))

# create student list
stu = [i for i in range(1, n+1)]

# initialize the number
num = 0
i = 0

# run loop until there's only one student on the table
while len(stu) != 1:
    # test if current id report 3
    isThird = False
    num += 1
    # report 3, then remove the id
    if num == 3:
        stu.remove(stu[i])
        num = 0
        isThird = True
    
    # if current id report 3, don't move to next position
    if not isThird:
        i+=1
    if i == len(stu):
        i=0

print("The last ID is:", stu[0])

