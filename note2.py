score = int(input("점수에 따라 받는 상품 다름"))

if score >= 100:
    print("자동차")
elif score >= 50:
    print("컴퓨터")
elif score >= 30:
    print("시계")
else:
    print("초코파이")