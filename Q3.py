import random

# 재시작 했을 때 이거 안나옴
print("숫자 야구 게임을 시작합니다.")

while True:

    # 숫자야구에 대한 이해도가 부족함
    answer = random.randrange(100, 1000)
    answer = str(answer)
    errorCount = 0

    while(errorCount < 3):
        flag = False
        try:
            num = int(input("숫자를 입력해주세요 : "))
            if (num < 100 or num > 999):
                errorCount += 1
                continue

            strike = 0
            ball = 0
            strNum = str(num)
            for i in range(0, 3):
                for j in range(0, 3):
                    if (answer[i] == strNum[j]):
                        if (i == j):
                            strike += 1
                        else:
                            ball += 1
                        continue
            
            if (strike == 0 and ball == 0):
                print("OUT")
            elif (strike == 3):
                print("3개의 숫자를 모두 맞히셨습니다! 게임이 종료됩니다!")
                next = input()
                
                if next == "Y":
                    break
                else:
                    flag = True
                    break
            else: 
                if (ball > 0):
                    print(str(ball)+"B", end="")
                if (strike > 0):
                    print(str(strike)+"S", end="")
                print("\n")
            

        # 불필요한 코드
        except:
            errorCount += 1

        if (flag):
            break
