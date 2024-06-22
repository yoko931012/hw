# input
layer = int(input("Enter the numbers of layers (2 to 5) = "))
top_length = int(input("Enter the side length of the top layer = "))
gr = int(input("Enter the growth of each layer = "))
trunk_width = int(input("Enter the trunk width (odd number, 3 to 9) = "))
trunk_height = int(input("Enter the trunk height (4 to 10) = "))

l = 0
# length of @ in the first layer
len_at = top_length - 2
# the widest tree length
max_width = top_length*2-1 + gr*(layer-1)*2
space = int(max_width/2)

while l < layer:
    # in the first layer, we have to put a # in the middle
    if l == 0:
        print(" " * space, end="")
        print("#")
    
    cur_len = 0
    #the number of #
    num = 1

    while cur_len < (len_at + gr*l):
        #calculate how much spaces are in front of the #
        num_space = int((max_width - (num+2))/2)
        #print spaces and layer
        print(" " * num_space, end="")
        print("#" + "@" * num + "#")
        cur_len += 1
        num += 2

    #print the bottom # layer
    bot_num = top_length*2-1 + gr*l*2
    print(" " * int((max_width - bot_num)/2), end="")
    print("#" * bot_num)
    l += 1

tr_l = 1
# print the trunk layer
while tr_l <= trunk_height:
    print(" " * int((max_width-trunk_width)/2), end="")
    print("|" * trunk_width)
    tr_l += 1