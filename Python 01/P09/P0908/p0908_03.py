# 클래스 연습하기

class Student:

    def __init__(self, no, name, kor, eng, math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.average = (kor + eng + math) / 3

    # 리스트 값 출력하기
    def __str__(self):
        return f"번호: {self.no}, 이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, 수학: {self.math}, 총점: {self.total}, 평균: {self.average:.2f}"



# 객체 선언
s1 = Student(1, "홍길동", 100, 90, 60)
s2 = Student(2, "유관순", 90, 100, 75)

# 리스트에 추가
stuList = []
stuList.append(s1)
stuList.append(s2)
s1.kor = 80

# 리스트 값 출력하기
for s in stuList:
    print(s)

# 결과값은 
# 번호: 1, 이름: 홍길동, 국어: 80, 영어: 90, 수학: 60, 총점: 250, 평균: 83.33
# 번호: 2, 이름: 유관순, 국어: 90, 영어: 100, 수학: 75, 총점: 265, 평균: 88.33

