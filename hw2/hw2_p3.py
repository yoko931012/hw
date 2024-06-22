# input
y = input("Please input Year: ")
m = int(input("Please input Month: "))

# 判斷閏平年
leap = True
ye = int(y)
if ye % 4 != 0:
    leap = False
elif ye % 100 == 0 and ye % 400 != 0:
    leap = False

# Week = (C + Y + M + D) mod 7
# setting parameters
year = y[-2] + y[-1]
# 年分可能有三位數、四位數
centery = int(y.replace(year, ""))
year = int(year)
month = m
day = 1

#calculate C, Y, M, D
C = 2 * (3 - (centery % 4))
Y = int((year % 28 + (year % 28 / 4)) % 7)
M = int(((3.4 + (month-3)%12 * 2.6)) % 7)
D = day % 7

# 閏年1、2月份 Y-1， 1、2月份 M-1
if (leap and month == 1) or month == 2:
    Y -= 1
if month == 1 or month == 2:
    M -= 1

# 第一天的星期
week = int((C + Y + M + D) % 7)

# 計算一個月幾天
if month == 1:
    days = 31
elif month == 2:
    if leap:
        days = 29
    else:
        days = 28
elif month == 3:
    days = 31
elif month == 4:
    days = 30
elif month == 5:
    days = 31
elif month == 6:
    days = 30
elif month == 7:
    days = 31
elif month == 8:
    days = 31
elif month == 9:
    days = 30
elif month == 10:
    days = 31
elif month == 11:
    days = 30
elif month == 12:
    days = 31

print("Sun Mon Tue Wed Thu Fri Sat")
print("    " * week, end="")

# a month start from day1
day = 1
while day <= days:
    # ensure we output two numbers
    print(str(day).rjust(2, '0'), end='  ')
    day += 1
    # meet Saturday, then start a new line
    if week == 6:
        print("")
        week = 0
        continue
    week += 1
