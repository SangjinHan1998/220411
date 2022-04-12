#  한국어 배우기 코드 업그레이드

list2 = ["감사", "끈기", "노력", "열정"]

# 점수
score = 0


for word in list2:
    print(word)
    data = input()
    if data == word:  # 문제를 맞힌 경우
        score += 1  # 점수를 1점 추가
        
print("전체 문제 갯수:", len(list2))
print("맞힌 갯수: ", score)  
print("틀린 갯수:", len(list2) - score)
        
    
    