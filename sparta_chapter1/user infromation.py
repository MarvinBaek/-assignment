class Person : #'person'이라는 클래스 정의
    def __init__(self, name, gender, age): #name,gender,age 각각 초기화하고 각 매개변수로 받기
        self.name = name
        self.gender = gender
        self.age = age
    
    def display(self): #정보 출력 메서드 정의
        return f"이름:{self.name}, 성별: {self.gender}\n나이: {self.age}"

while True:
    try:
        age = int(input("나이: "))  # 나이 입력받기
        if age <= 0:
            print("나이는 0보다 큰 값이어야 합니다.")
        else:
            break
    except ValueError: #부적절한 값을 인자로 받았을 때 
        print("숫자만 입력해 주세요")
        
name = input("이름: ") # 이름 입력받기

while True: #성별 입력받기
    gender = input("성별(남/여 또는 male/female): ")
    if gender in ['남','여','male', 'female']:
        if gender == '남' or gender == 'male':
            gender = "male"
        elif gender== '여' or gender =="female":
            gender = "female"
        break
    else:
        print("잘못된 입력입니다. 남,여 또는 male/femal 중 입력해 주세요.")

per1 = Person(name,gender,age) #Person 객체 생성

print(per1.display()) #정보 출력
