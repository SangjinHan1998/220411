# while 
# 보통 반복 횟루가 정해지지 않았을 때 사용한다. 

i = 0 # 초기식
while i < 10: # 조건식
    print(i, "times promise, I can do it!!!")
    i += 1 # 증감식 

print("========================================")
i = 5 # 초기식의 값을 바꿔 출력값을 바꾼다. 
while i < 19: # 조건식의 값을 바꿔 출력값을 바꾼다. 
    print(i, "times promise, I can do it!!!")
    i += 2 # 증감식의 값을 바꿔 출력값을 바꾼다. 
    
# 무한루프 
# 조건식에 True 를 넣어서 항상 반복되게 만든 것. 

print("========================================")
while True:
    x = input("If you want to quit, Input [exit] ")
    if x == "exit":
        break