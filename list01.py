list1 = ["일", "이", "삼", "사", "오", "육", "칠",]
print(list1)
# 데이터 추가 list.append(data)
list1.append("팔")
print(list1)
# 데이터 할당 list[index] = data
list1[1] = "two"
print(list1)
# 데이터 삭제 del list[index] 
del list1[3]
print(list1)
# 슬라이싱  list[시작:끝+1]
print(list1[3:7])
print(list1[:])# 전체 다 가져와라
print(list1[:3]) # 3-1번째 데이터 가져오기
# 리스트 길이 len(list)
print(len(list1))
# 리스트 정렬 list.sort()
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)