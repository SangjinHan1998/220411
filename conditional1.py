#조건문
# : 조건에 따라 실행할 명령이 달라짐
# 이 과정에서 비교연산이 사용됨 조건에 따른 경우 만들기

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

if input_pass ==  origin_pass:  # 조건 A
    # 조건 A 참
    print("로그인 성공")
    print("Correct Log In")
elif input_pass == "":
    # 조건 A 거짓, 조건 B 참
    print("No Data")
else:
    # 조건 A 거짓 조건 B 거짓
    print("로그인 실패")
    print("비밀번호 확인")
    
