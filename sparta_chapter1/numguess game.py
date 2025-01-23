import random #random 함수를 사용하기 위해 import

com = random.randrange(1,11) #컴퓨터에게 1이상 10 사이에서 랜덤한 숫자 선택

print("1과 10 사이의 숫자를 하나 정했습니다.\n 이 숫자는 무엇일까요?" )

while True: # 사용자가 정답을 맞출 때까지 반복
    try:
        person = int(input("예상숫자:")) #사용자에게 숫자받고 비교를 위해 int형으로 변환
    except ValueError:
        print("숫자를 입력해 주세요.")
        continue #숫자가 아닌 입력이 들어오면 다시 시도

    if com < person: #컴퓨터와 사람 입력 숫자 비교
        print("너무 큽니다. 다시 입력하세요")

    elif com > person:
        print("너무 작습니다. 다시 입력하세요")

    else: # com == person인 경우
        print("정답입니다.")
        break #정답을 맞추면 반복문 종료
