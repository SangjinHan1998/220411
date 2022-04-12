kor, math, eng = map(int,input().split())

total = kor + math + eng
avg = total / 3

if 0 <= kor <= 100 and 0 <= math <= 100 and 0 <= eng <= 100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못입력")