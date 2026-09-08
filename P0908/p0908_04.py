# 클래스 함수 ~ 리스트에 입력해서 넣기

class Stud:

    def __init__(self, no, name, kor, eng, math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        # self.total = kor + eng + math
        # self.average = (kor + eng + math) / 3
        self.total = 0
        self.average = 0
        self.calc_sum()
        self.calc_avg()

    def __str__(self):
        return f"번호: {self.no}, 이름: {self.name}, 국어: {self.kor}, 영어: {self.eng}, 수학: {self.math}, 총점: {self.total}, 평균: {self.average:.2f}"

    def calc_sum(self):
        self.total = self.kor + self.eng + self.math
        return self.total
        
    def calc_avg(self):
        self.average = (self.kor + self.eng + self.math) / 3
        return self.average


stuList = []
while True:
    no = int(input("번호 입력: "))
    name = input("이름 입력: ")
    kor = int(input("국어 입력: "))
    eng = int(input("영어 입력: "))
    math = int(input("수학 입력: "))
    stuList.append(Stud(no, name, kor, eng, math))

    for s in stuList:
        print(s)

# 결과값은 번호: 1, 이름: 홍길동, 국어: 90, 영어: 70, 수학: 80, 총점: 240, 평균: 80.00

# 이어서 치면 결과가 계속 붙어나옴 (리스트이기 때문?)
# 번호: 2, 이름: 유관순, 국어: 90, 영어: 70, 수학: 85, 총점: 245, 평균: 81.67
# 번호: 3, 이름: 이순신, 국어: 70, 영어: 90, 수학: 80, 총점: 240, 평균: 80.00