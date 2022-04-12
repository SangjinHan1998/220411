# 시퀀스 자료형
# 순서가 있는 자료형 
# -리스트
# -문자열
# -range객체
# 튜플
# 딕셔너리

# for 문
# 리스트 사용
champions = ["티모", "자르반4세", "렉사이"]

for champion in champions:
    print("You selected" , champion, ".Is it right??")
    
# for 문은 데이터 반복할때까지 진행되고 데이터가 없으면 종료된다. 

cheerUp_msg = "If you want to give up, Ignore your mind. It's trick."
for word in cheerUp_msg:
    print(word)
    
# - range 객체 사용
# range(10) -> 0~9 까지 숫자를 포함하는 range 객채 나온다. 0,1,2,3,4,5,6,7,8,9
# range(시작, 끝 + 1, 단계)
for i in range(1,10,2): # 2(두칸씩 띄어서 출력)
    print(i)
