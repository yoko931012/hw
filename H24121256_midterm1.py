#打印第一串
i = 9 #前面的數字從9開始
while 1 <= i <= 9:#第一串前面的數字從1到9
	j = 9#後面的數字也從9
	print(i,"x",j,"=",i*j,end = "\t")
	print(i,"x",(j-1),"=",i*(j-1),end = "\t")
	print(i,"x",(j-2),"=",i*(j-2),end = "\n")
	j -= 1
	print()
	i -= 1
print(end = "\n")#第一串結束的分界
#打印第二串	
i = 9
while 1 <= i <= 9:
	j = 6
	print(i,"x",j,"=",i*j,end = "\t")
	print(i,"x",(j-1),"=",i*(j-1),end = "\t")
	print(i,"x",(j-2),"=",i*(j-2),end = "\n")
	j -= 1
	print()
	i -= 1
print(end = "\n")#第二串結束的分界
#打印第三串
i = 9
while 1 <= i <= 9:
	j = 3
	print(i,"x",j,"=",i*j,end = "\t")
	print(i,"x",(j-1),"=",i*(j-1),end = "\t")
	print(i,"x",(j-2),"=",i*(j-2),end = "\n")
	j -= 1
	print()
	i -= 1




