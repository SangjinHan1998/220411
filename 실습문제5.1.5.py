#구구단 출력하기

# 1. while 
x = int(input("몇 단을 출력할까요"))

i = 1
while i < 10:
    print(x ,"*", i , "=", x*i )
    i += 1

# 2. for
y = int(input("몇단출력???"))

for j in range(1, 10):
    print(y, "*" , j, "=", y * j)
    