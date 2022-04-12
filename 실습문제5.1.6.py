# 메뉴 출력문제

while True:
    print("[input Menu]")
    x = int(input("1.Start Game 2. Look Leaderboards 3.Exit Game"))
    if x == 1:
        print("->Start Game ")
    elif x == 2:
        print("->Look Leaderboards")
    elif x == 3:
        print("->Exit game")
        break
    else:
        print("input again please.")