# input
X, Y, k = list(map(int, input("Enter index x, y, k (seperated by space): ").split()))
r_color = str(k)

# initialize image matrix
image = []
print("Enter the matrix by multiple lines: ")

# input matrix
while True:
    row = input().split()
    if row == ["q"]:
        break
    image.append(row)


color = image[X][Y]
# create a coordinate set including all adjacent pixels' coordinates
# we will traverse the set to find out which pixels are the same color and delete them 
coor = [[X, Y]]

while len(coor):
    x = coor[0][0]
    y = coor[0][1]

    if image[x][y] == color:
        # replace color with k color
        image[x][y] = r_color

        # find out the adjacent pixels in x-axis
        if x > 0:
            coor.append([x-1, y])
        if x < len(image)-1:
            coor.append([x+1, y])
        
        # find out the adjacent pixels in y-axis
        if y > 0:
            coor.append([x, y-1])
        if y < len(image)-1:
            coor.append([x, y+1])

    del coor[0]

for r in image:
    row = " ".join(r)
    print(row)
